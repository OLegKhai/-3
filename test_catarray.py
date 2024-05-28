import pytest
from cat import Cat, CatArray
from abstractstructure import AbstractCatArray

def test_cat_initialization():
    cat = Cat("Барсик", "Персидська", "білий", 0.3, 1.5, "довгошерстий")
    assert cat.name == "Барсик"
    assert cat.breed == "Персидська"
    assert cat.color == "білий"
    assert cat.age == 0.3
    assert cat.weight == 1.5
    assert cat.category == "довгошерстий"

def test_catarray_initialization():
    cat1 = Cat("Барсик", "Персидська", "білий", 0.3, 1.5, "довгошерстий")
    cat_array = CatArray([cat1])
    assert len(cat_array) == 1
    assert cat_array[0] == cat1

def test_catarray_append():
    cat1 = Cat("Барсик", "Персидська", "білий", 0.3, 1.5, "довгошерстий")
    cat2 = Cat("Мурзик", "Сіамська", "сірий", 2, 4.5, "короткошерстий")
    cat_array = CatArray([cat1])
    cat_array.append(cat2)
    assert len(cat_array) == 2
    assert cat_array[1] == cat2

def test_catarray_insert():
    cat1 = Cat("Барсик", "Персидська", "білий", 0.3, 1.5, "довгошерстий")
    cat2 = Cat("Мурзик", "Сіамська", "сірий", 2, 4.5, "короткошерстий")
    cat3 = Cat("Том", "Британська", "чорний", 1, 3, "короткошерстий")
    cat_array = CatArray([cat1, cat3])
    cat_array.insert(1, cat2)
    assert len(cat_array) == 3
    assert cat_array[1] == cat2

def test_catarray_index():
    cat1 = Cat("Барсик", "Персидська", "білий", 0.3, 1.5, "довгошерстий")
    cat_array = CatArray([cat1])
    assert cat_array.index(cat1) == 0
    with pytest.raises(ValueError):
        cat_array.index(Cat("Мурзик", "Сіамська", "сірий", 2, 4.5, "короткошерстий"))

def test_catarray_remove():
    cat1 = Cat("Барсик", "Персидська", "білий", 0.3, 1.5, "довгошерстий")
    cat2 = Cat("Мурзик", "Сіамська", "сірий", 2, 4.5, "короткошерстий")
    cat_array = CatArray([cat1, cat2])
    cat_array.remove(cat1)
    assert len(cat_array) == 1
    assert cat_array[0] == cat2
    with pytest.raises(ValueError):
        cat_array.remove(cat1)

if __name__ == "__main__":
    pytest.main()
