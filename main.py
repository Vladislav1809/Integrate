import interface
from tkinter import Entry, StringVar, Label
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

matplotlib.use('TkAgg')


def main():
    root = interface.Tk()
    Label(root, text="Исследуемый интеграл:", height=0, width=5).pack(fill=interface.BOTH, padx=2, pady=5)
    label = Label(root).pack()
    fig = matplotlib.figure.Figure(figsize=(0.6, 0.6), dpi=100)
    ax = fig.add_subplot(111)

    canvas = FigureCanvasTkAgg(fig, master=label)
    canvas.get_tk_widget().pack(side="top", fill="both", expand=True)
    canvas.tkcanvas.pack(side="top", fill="both", expand=True)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    ax.clear()
    ax.text(0.38, 0.4, r'$\int_{0}^{2R}\frac{\sqrt{z(2R-z)}dz}{\sqrt{z+h}}$', fontsize=13)
    canvas.draw()

    rad_text = Label(root, text='Введите радиус:', height=2, width=5)
    radius = StringVar()
    radius_entry = Entry(root, textvariable=radius)
    rad_text.pack(fill=interface.BOTH, padx=5, pady=5)
    radius_entry.pack(fill=interface.BOTH, padx=5, pady=5)

    h_text = Label(root, text='Введите высоту патрубка:', height=2, width=5)
    h = StringVar()
    h_entry = Entry(root, textvariable=h)
    h_text.pack(fill=interface.BOTH, padx=10, pady=10)
    h_entry.pack(fill=interface.BOTH, padx=5, pady=5)

    root.geometry("700x400")
    interface.Window(root, radius, h)
    root.mainloop()


if __name__ == '__main__':
    main()
