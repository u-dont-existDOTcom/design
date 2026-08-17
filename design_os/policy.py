"""Pure policy primitives shared by the design workflow and its tools."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, Sequence

SURFACE_MODES: tuple[str, ...] = (
    "persuade",
    "operate",
    "read",
    "experience",
)

PERCEPTUAL_LAYERS: tuple[str, ...] = ("L0", "L1", "L2", "L3", "L4")

AUTHORITY_ORDER: tuple[str, ...] = (
    "explicit-user-truth",
    "project-context",
    "correctness-accessibility-ethics-law",
    "lower-perceptual-layers",
    "implementation-boundaries",
    "project-identity",
    "searched-guidance",
    "anti-pattern-heuristics",
    "agent-taste",
)


@dataclass(frozen=True, slots=True)
class Candidate:
    """A proposed direction and the requirements it still fails."""

    name: str
    score: float
    unmet_requirements: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("Candidate name cannot be empty.")
        if not 0.0 <= self.score <= 1.0:
            raise ValueError("Candidate score must be between 0.0 and 1.0.")


@dataclass(frozen=True, slots=True)
class DirectionDecision:
    """Whether the workflow should continue automatically or ask a human."""

    action: Literal["select", "ask"]
    selected: str | None
    reason: str


def choose_direction(
    candidates: Sequence[Candidate], dominance_margin: float = 0.12
) -> DirectionDecision:
    """Choose a valid clear winner, otherwise preserve the human decision gate."""

    if not 0.0 <= dominance_margin <= 1.0:
        raise ValueError("dominance_margin must be between 0.0 and 1.0.")

    survivors = sorted(
        (candidate for candidate in candidates if not candidate.unmet_requirements),
        key=lambda candidate: (-candidate.score, candidate.name.casefold()),
    )
    if not survivors:
        return DirectionDecision(
            action="ask",
            selected=None,
            reason="No candidate satisfies every non-negotiable requirement.",
        )
    if len(survivors) == 1:
        return DirectionDecision(
            action="select",
            selected=survivors[0].name,
            reason="Only one candidate survives every requirement.",
        )

    lead = survivors[0].score - survivors[1].score
    if lead >= dominance_margin:
        return DirectionDecision(
            action="select",
            selected=survivors[0].name,
            reason=(
                f"The selected candidate clearly dominates by {lead:.2f}, "
                f"meeting the {dominance_margin:.2f} continuation margin."
            ),
        )
    return DirectionDecision(
        action="ask",
        selected=None,
        reason="Materially competing candidates remain after requirement filtering.",
    )


def applicable_states(
    *,
    interactive: bool,
    fine_pointer: bool,
    asynchronous: bool,
    reports_outcome: bool,
) -> tuple[str, ...]:
    """Return only interaction states that apply to the component's semantics."""

    if not interactive:
        return ("default",)

    states = ["default"]
    if fine_pointer:
        states.append("hover")
    states.extend(("focus-visible", "active", "disabled"))
    if asynchronous:
        states.append("loading")
    if asynchronous or reports_outcome:
        states.extend(("error", "success"))
    return tuple(states)
