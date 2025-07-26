# 📞 Lista Telefônica - Advanced Contact Manager

A comprehensive contact management system built in Python with Object-Oriented Programming principles. Features persistent data storage, advanced contact operations, and a user-friendly CLI interface for managing personal and professional contacts efficiently.

## 📸 Preview

```
==================================================
           LISTA TELEFÔNICA
==================================================
1. Adicionar contato
2. Visualizar todos os contatos
3. Editar contato
4. Marcar/Desmarcar favorito
5. Ver contatos favoritos
6. Remover contato
7. Sair

--- TODOS OS CONTATOS (3) ---
1. João Silva ⭐ | Tel: (11) 99999-9999 | Email: joao@email.com
2. Maria Santos | Tel: (11) 88888-8888
3. Pedro Costa ⭐ | Tel: (11) 77777-7777 | Email: pedro@email.com
```

## 📋 About This Project

This project is an advanced contact management system that demonstrates sophisticated Python programming concepts through Object-Oriented Programming, file handling, and data persistence. The application provides a complete contact management solution with favorites system, data validation, and persistent JSON storage.

### Core Features:
- **Complete Contact Management**: Add, view, edit, and remove contacts
- **Favorites System**: Mark important contacts with star indicators
- **Persistent Storage**: Automatic JSON file saving and loading
- **Data Validation**: Duplicate prevention and input validation
- **Advanced Search**: Name-based contact lookup
- **Professional Interface**: Clean CLI with organized menus

## 🛠️ Technologies Used

- **Python 3** - Core programming language with advanced features
  - **Object-Oriented Programming**: Classes and methods
  - **Type Hints**: Enhanced code readability and IDE support
  - **JSON Handling**: Data serialization and file persistence
  - **File I/O Operations**: Reading and writing contact data
  - **Exception Handling**: Robust error management
  - **List Comprehensions**: Efficient data filtering

## 🎯 Features

- ✅ **Object-Oriented Architecture** - Clean class-based design
- ✅ **Persistent Data Storage** - JSON file-based contact storage
- ✅ **Favorites Management** - Star system for important contacts
- ✅ **Duplicate Prevention** - Name-based uniqueness validation
- ✅ **Advanced Editing** - Selective field updates
- ✅ **Data Validation** - Input verification and error handling
- ✅ **Sorted Display** - Alphabetically ordered contact lists
- ✅ **Confirmation Systems** - Safe deletion with user confirmation

## 🔧 Installation & Usage

1. **Clone the repository**
   ```bash
   git clone https://github.com/xManoelx/python-phone-book.git
   cd python-phone-book
   ```

2. **Run the application**
   ```bash
   python lista_telefonica.py
   ```

3. **Using the application**
   - Navigate through numbered menu options
   - Add contacts with name, phone, email, and favorite status
   - Edit existing contacts with selective field updates
   - Mark/unmark favorites with star indicators
   - View all contacts or filter by favorites
   - Remove contacts with confirmation prompts

## 🏗️ Architecture Overview

### Class Structure:

**`Contato` Class:**
- Represents individual contact objects
- Handles data serialization/deserialization
- Provides string representation with favorites indication

**`ListaTelefonica` Class:**
- Manages contact collection and operations
- Handles file I/O and data persistence
- Provides CRUD operations with validation

**Menu Functions:**
- Modular interface functions for each operation
- Input validation and user feedback
- Error handling and confirmation dialogs

## 💾 Data Persistence

The application automatically saves all contacts to `contatos.json`:

```json
[
  {
    "nome": "João Silva",
    "telefone": "(11) 99999-9999",
    "email": "joao@email.com",
    "favorito": true
  }
]
```

## 📚 What I Learned

This project significantly advanced my Python skills in:

- **Object-Oriented Programming**: Class design, inheritance, and encapsulation
- **Type Hints**: Modern Python type annotation practices
- **File Handling**: JSON serialization and persistent data storage
- **Error Handling**: Comprehensive exception management
- **Data Validation**: Input verification and business logic
- **Code Organization**: Modular design and separation of concerns
- **User Experience**: Intuitive CLI interface design

## 🌟 Technical Highlights

- **Advanced OOP Design**: Clean class architecture with proper encapsulation
- **Type Safety**: Comprehensive type hints for better code quality
- **Data Persistence**: Automatic JSON file handling with error recovery
- **Business Logic**: Duplicate prevention and data validation
- **User Interface**: Professional CLI with clear feedback and confirmation
- **Error Recovery**: Graceful handling of file errors and invalid input

## 🔄 Advanced Features

- **Smart Editing**: Update only specified fields while preserving others
- **Alphabetical Sorting**: Automatic contact ordering for easy browsing
- **Favorites Filtering**: Quick access to important contacts
- **Confirmation Dialogs**: Safe deletion with user verification
- **Data Recovery**: Automatic handling of corrupted or missing files

## 🚀 Code Quality Features

- **Type Hints**: Enhanced IDE support and code documentation
- **Modular Design**: Separated concerns with dedicated functions
- **Error Handling**: Comprehensive exception management
- **Data Validation**: Input verification at multiple levels
- **Clean Code**: Readable variable names and clear function purposes

## 🔄 Future Improvements

- [ ] Add contact search by phone number or email
- [ ] Implement contact categories and tags
- [ ] Add data import/export functionality (CSV, vCard)
- [ ] Create contact backup and restore features
- [ ] Add contact photo support
- [ ] Implement contact sharing capabilities
- [ ] Add contact history and modification tracking

## 👨‍💻 Author

**Manoel Antonio**
- Junior Robot Programmer transitioning to Full Stack Development
- GitHub: [@xManoelx](https://github.com/xManoelx)
- Location: Caxias do Sul, RS, Brasil

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

*From industrial automation to contact management systems - applying advanced Python concepts to solve real-world problems! 🤖📞*
