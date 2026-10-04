from pathlib import Path

def test_three_notebooks_planned():
    readme = Path(__file__).parent.parent / "notebooks" / "README.md"
    text = readme.read_text(encoding="utf-8")
    assert "01_tensor_mastery" in text
    assert "02_autograd_tour" in text
    assert "03_train_mlp" in text
