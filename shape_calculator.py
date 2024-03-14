#coding:utf-8
"""

Polygon Area Calculator

"""
# Class


class Rectangle:

  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"

  def set_width(self, newwidth):
    self.width = newwidth

  def set_height(self, newheight):
    self.height = newheight

  def get_area(self):
    self.area = self.width * self.height
    return self.area

  def get_perimeter(self):
    self.perimeter = 2 * self.width + 2 * self.height
    return self.perimeter

  def get_diagonal(self):
    diagonal = (self.width**2 + self.height**2)**.5
    return diagonal

  def get_picture(self):
    if self.height >= 50 or self.width >= 50:
      return "Too big for picture."

    else:

      width_print = "*" * self.width
      height_print = self.height

      Picture = f"{width_print}\n" * height_print

      return Picture

  def get_amount_inside(self, shape2):

    # compare their perimeter

    if self.width >= shape2.width and self.height >= shape2.height:
      fit_width = self.width // shape2.width
      fit_height = self.height // shape2.height

      amout_inside = fit_width * fit_height
      return amout_inside

    else:
      return 0


class Square(Rectangle):

  def __init__(self, side):

    super().__init__(side, side)

    self.side = side

  def __str__(self):
    return f"Square(side={self.side})"

  def set_side(self, newside):
    self.side = newside
    self.height = newside
    self.width = newside

  def set_height(self, newheight):
    self.side = newheight
    self.height = newheight
    self.width = newheight

  def set_width(self, newwidth):
    self.side = newwidth
    self.height = newwidth
    self.width = newwidth
        
        
        
    def __str__(self):
        return f"Square(side={self.side})"

    
    
    def set_side (self,newside):
        self.side = newside
        self.height = newside
        self.width = newside
        
        print(f"\nNew side is {self.side}")

    def set_height (self,newheight):
        self.side = newheight
        self.height = newheight
        self.width = newheight
        
        print(f"\nNew side is {self.side}")

    def set_width (self,newwidth):
        self.side = newwidth
        self.height = newwidth
        self.width = newwidth
        
        print(f"\nNew side is {self.side}")

    
        

       


# Main Code

rect = Rectangle(10,3)

print(rect.get_picture())