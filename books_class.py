class books:
  def __init__(self,title,author,year):
    self.title=title
    self.author=author
    self.year=year
  def display_info(self):
    print(f"Title: {self.title}")
    print(f"Author: {self.author}")
    print(f"Year: {self.year}")
  author1=books("The Great Gatsby","F. Scott Fitzgerald",1925)
  author1.display_info()
