
from tkinter import *

root =Tk()

root.geometry("444x234")
root.title("My GUI with AJay")

# text - add the text
# bd - background
# fg- forground
# font - sets the font
# padx - x padding
# pady - y padding
# releif - border styling - SUNKEN,RAISED,GROOVE,RIDGE

title_label = Label(text = '''Abdul Rashid Salim Salman Khan ; Hindi: 
\nAbout this soundpronunciation (help·info); 27 December 1965)[4] is an Indian film actor, producer, 
\noccasional singer and television personality. In a film career spanning over thirty years, 
\nKhan has received numerous awards, including two National Film Awards as a film producer, 
\nand two Filmfare Awards for acting.[5] He has a significant following in Asia and the 
\nIndian diaspora worldwide,[6][better source needed] and is cited in the media as one of the most commercially successful 
\nactors of both world and Indian cinema.[7][8] According to the Forbes 2018 list of Top-Paid 100 Celebrity 
\nEntertainers in world, Khan was the highest ranked Indian with 82nd rank with earnings of $37.7 
\nmillion.[9][10] He is also known as the host of the reality show, Bigg Boss since 2010.[11]''',
                    bg = 'red',fg = 'black', padx =23,pady =34,font = "comicsansms 10 italic",borderwidth =3,relief=SUNKEN)

#Important Pack attribute
#anchor = nw
#side = top, bottom,left ,right


title_label.pack(anchor= 'ne',side = 'bottom',fill = Y,padx=23,pady=44)

root.mainloop()