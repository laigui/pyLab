import Tkinter,tkFileDialog

myFormats = [
    ('Windows Bitmap','*.bmp'),
    ('Portable Network Graphics','*.png'),
    ('JPEG / JFIF','*.jpg'),
    ('CompuServer GIF','*.gif'),
    ]

root = Tkinter.Tk()
fileName = tkFileDialog.asksaveasfilename(parent=root,filetypes=myFormats ,title="Save the image as...")
if len(fileName) > 0:
    print "Now saving under %s" %(fileName)