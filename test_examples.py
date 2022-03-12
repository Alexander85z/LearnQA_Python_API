class TestExample:
    def test_len_name(self):
        len_name= input("Введите фразу не больше 15 символов:")
        assert len(len_name) < 15