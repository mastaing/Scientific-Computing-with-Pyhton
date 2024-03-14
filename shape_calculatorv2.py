#coding:utf-8


"""

Polygon Area Calculator

"""
# Class

class Rectangle :
    
    def __init__(self, width, height) :
        self.width = width
        self.height = height

    def __str__(self) :
        return f"Rectange(width={self.width}, height={self.height})"

    def set_widht (self, newwidth) :
        self.width = newwidth 
        print(f"\nNew width is {self.width}")
    
    def set_height (self, newheight) : 
        self.height = newheight
        print(f"\nNew height is {self.height}")
    
    def get_area (self) :
        self.area = self.width*self.height
        return f"\nArea : {self.area}"
    
    def get_perimeter (self) :
        self.perimeter = 2*self.width + 2*self.height
        return f"\nPerimeter : {self.perimeter}"
    
    def get_diagonal (self) :
        self.diagonal = round((self.width**2 + self.height**2) **.5,3)
        return f"\nDiagonal : {self.diagonal}"
    
    def get_picture (self) :
        if self.height >= 50 or self.width >= 50 :
            return "Too big picture."
        else :
            width_print = "* "*self.width
                       
            compteur_height = 0
            
            while compteur_height < self.height :
                print (width_print)
                compteur_height += 1
            
    
    def get_amout_inside (self,shape2) :
        
        # compare their perimeter
        

        if self.width >= shape2.width and self.height >= shape2.height :
            fit_width = self.width // shape2.width
            fit_height = self.height // shape2.height

            amout_inside = fit_width * fit_height
            return f"you can fit {amout_inside} times the {shape2} inside the {self} "

        else :
            return f"couldn't fit in the {self}"

class Square(Rectangle):
    def __init__(self,side):
        
        super().__init__(side, side)

        self.side = side
        
        
        
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

    def set_widht (self,newwidth):
        self.side = newwidth
        self.height = newwidth
        self.width = newwidth
        
        print(f"\nNew side is {self.side}")

    
        

       


# Main Code

rect = Rectangle(60,60)
print(rect)
rect.set_height(8)
print(get_picture(rect))

