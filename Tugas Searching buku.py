# daftar buku perpustakaan (data buku)
library = []

def add_book():
    # Fungsi untuk menambahkan buku ke dalam perpustakaan
    title = input("Masukkan judul buku: ")
    author = input("Masukkan nama penulis: ")
    year = input("Masukkan tahun terbit: ")

    book = {"title": title, "author": author, "year": year}
    library.append(book)
    print(f"Buku '{title}' berhasil ditambahkan ke perpustakaan!")

def search_books(keyword, field):
    # Fungsi untuk mencari buku berdasarkan kata kunci
    results = []
    for book in library:
        if keyword.lower() in book[field].lower():
            results.append(book)
    return results

def display_books(books):
    # Fungsi untuk menampilkan daftar buku
    if not books:
        print("Tidak ada buku yang ditemukan.")
    else:
        print("Buku yang ditemukan:")
        for book in books:
            print(f"Judul: {book['title']}, Penulis: {book['author']}, Tahun: {book['year']}")

def display_all_books(): 
    # Fungsi untuk menampilkan semua buku yang ada di perpustakaan
    if not library:
        print("Tidak ada buku dalam perpustakaan.")
    else:
        sorted_books = sorted(library, key=lambda x: (x["title"].lower(), x["year"].lower))
        display_books(sorted_books)

def main():
    while True:
        print("\nMenu perpustakaan:")
        print("1. Tambah Buku")
        print("2. Tampilkan Semua Buku")
        print("3. Cari Buku")
        print("4. Keluar")
        choice = input("Pilihan menu (1/2/3/4): ")

        if choice == "1":
            add_book()
        elif choice == "2":
            display_all_books()
        elif choice == "3":
            print("1. Cari buku berdasarkan judul")
            print("2. Cari buku berdasarkan penulis")
            print("3. Cari buku berdasarkan tahun")
            search_choice = input("Pilihan menu (1/2/3): ")
            if search_choice == "1":
                keyword = input("Masukkan judul buku yang ingin dicari: ")
                results = search_books(keyword, "title")
                display_books(results)
            elif search_choice == "2":
                keyword = input("Masukkan penulis buku yang ingin dicari: ")
                results = search_books(keyword, "author")
                display_books(results)
            elif search_choice == "3":
                keyword = input("Masukkan tahun terbit yang ingin dicari: ")
                results = search_books(keyword, "year")
                display_books(results)
            else:
                print("Pilihan tidak valid.")
        elif choice == "4":
            print("Terima kasih telah menggunakan perpustakaan!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
