fn main() {
    
}
   //Владение//
//Стек: последний вошёл - первый вышел
//Куча: Место выделяется самостоятельно и всё медленно и разбросано
//У каждого значения есть только один владелец
//Когда мы выходим с какой-то области видимости, то её переменные, функции и прочее очищается
//Копирование - передача значения, хранящийся в стеке
//Перемещение - передача значения, хранящийся в куче, и самоудаление
//String.clone() - клонирование
//  _________Стек________
// /      |      |    \  кортежи со всеми этими типами
//дробные |      |     \_
//     целые  без знака  булевые
//Когда кучевые занчения указывают как аргумент функции они перемещаются
//Возвращаемое значение функции _перемещается_ в указанную переменную
   //Ссылки//
//String = значение &String = ссылка
//Ссылки - крутые, они передают значение без потерь производительности и памяти
//Но ссылки по умолчанию не изменяемы, &mut String - будет изменяться
//String.push_str("...") - конкатенация
//Нельзя использовать две изменяемых ссылки на одну переменную
//Можно дофегища раз использовать обычные ссылки!
//Висящая ссылка - ссылка на ничего
   //Срезы//
//Ссылочный тип данных &String[begin..end]
//Begin по умолчанию равен 0
//End по умолчанию равен самому последнему символу
   //Структуры//
//Следует создавать до функции мейн
//struct _ {
//	ключ: тип значения,
//	ключ: тип значения,
//};
//Это как классики
//Отклонение: "...".to_string() - тоже можно
//#[derive(Debug)] - это аннотация (хз), нужно для того, чтобы печатать структуру
//объект.значение - так обращаются к значению
//можно присваивать другие значения если сделать весь объект мутабельным
//если ключ совпадает с одной из переменной то можно написать имя той переменной и всё
//если ключи совпадают с переменными и объект уже когда-то создавался, то можно написать ..first_object и переменные сами подставятся под ключи
//Отклонение: число.sqrt() - корень квадратный
// impl имя структуры {
//	fn имя метода(&self){
//		бла-бла-бла
//	} без ;
//	другие методы...
//} - создание метода для структуры (метод Rust = метод JS = метод Python)
//Struct::func(...) - несвязанная функция, то, что не требует ссылки на структуру в аргументах
//можно создать несколько блоков impl
