# tests/test_hw05.py
import pytest
from hw05.main import parse_grid, grid_shortest_path

def test_parse_finds_start_and_target():
    lines = [
        "S..",
        ".#.",
        "..T"
    ]
    graph, start, target = parse_grid(lines)
    assert start == "0,0"
    assert target == "2,2"
    assert "0,1" in graph
    assert "1,1" not in graph  # wall

def test_basic_path():
    lines = [
        "S..",
        ".#.",
        "..T"
    ]
    p = grid_shortest_path(lines)
    assert p[0] == "0,0"
    assert p[-1] == "2,2"
    assert "1,1" not in p

def test_unreachable_returns_none():
    lines = [
        "S#.",
        "###",
        "..T"
    ]
    assert grid_shortest_path(lines) is None

def test_start_equals_target():
    lines = ["ST"]  # start at 0,0, target at 0,1
    p = grid_shortest_path(lines)
    assert p == ["0,0","0,1"]

@pytest.mark.parametrize("lines", [
    ["S....T"],
    ["S.T"]
])
def test_straight_line_lengths(lines):
    p = grid_shortest_path(lines)
    assert p[0].startswith("0,0")
    assert p[-1].endswith(str(len(lines[0])-1))

def test_larger_maze():
    # Solvable grid
    lines = [
        "S.#..",
        ".#...",
        "...T."
    ]
    p = grid_shortest_path(lines)
    assert p is not None
    assert p[0] == "0,0"
    assert p[-1] == "2,3"
    for cell in p:
        r, c = map(int, cell.split(","))
        assert lines[r][c] != "#"

def test_no_diagonals():
    lines = [
        "S#T",
        "###",
        "..."
    ]
    p = grid_shortest_path(lines)
    if p is not None:
        for i in range(len(p)-1):
            r1, c1 = map(int, p[i].split(","))
            r2, c2 = map(int, p[i+1].split(","))
            assert abs(r1 - r2) + abs(c1 - c2) == 1
