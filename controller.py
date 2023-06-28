import text
import view
import model

def start():
    while True:
        select = view.menu()
        match select:
            case 1:
                if model.open_file():
                    view.print_message(text.load_successful)
                else:
                    view.print_message(text.error_load)
            case 2:
                if model.save_file():
                    view.print_message(text.save_successful)
                else:
                    view.print_message(text.error_save)
            case 3:
                view.show_contacts(model.phone_book, text.empty_book)
            case 4:
                new = view.add_contact()
                model.add_contact(new)
                view.print_message(text.add_successful(new.get('name')))
            case 5:
                word = view.search_word()
                result = model.search(word)
                view.show_contacts(result, text.empty_search(word))
            case 6:
                word = view.search_word()
                result = model.search(word)
                view.show_contacts(result, text.empty_search(word))
                id = view.change_get_id()
                change = view.change_contact()
                print(change)
                model.change_contact(id, change)
                view.print_message(text.change_successful(change.get('name')))
            case 7:
                word = view.search_word()
                result = model.search(word)
                view.show_contacts(result, text.empty_search(word))
                id = view.delete_get_id()
                model.delete_contact(id)
                view.print_message(text.delete_successful(id))

            case 8:
                view.print_message(text.goodbye)
                break
