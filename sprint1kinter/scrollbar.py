import tkinter as tk

root = tk.Tk()
root.title("Ejercicio Scrollbar")
root.geometry("400x300")

frame = tk.Frame(root)
frame.pack(fill="both", expand=True, padx=10, pady=10)

texto= tk.Text(frame,wrap="word")
texto.pack(side="left", fill="both", expand=True)

scroll = tk.Scrollbar(frame, orient="vertical", command=texto.yview)
texto.config(yscrollcommand=scroll.set)


texto_largo = (
    "Párrafo 1:\n"
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur "
    "tempor, neque et suscipit cursus, urna nunc egestas lectus, ut "
    "fringilla tortor mi non lorem. Integer sit amet justo non sapien "
    "dignissim aliquam.\n\n"

    "Párrafo 2:\n"
    "Suspendisse potenti. Donec placerat, odio at facilisis tincidunt, "
    "erat lorem vulputate nibh, vitae dictum nisl sapien a purus. "
    "Phasellus vitae risus sit amet nibh suscipit varius.\n\n"

    "Párrafo 3:\n"
    "Mauris non arcu vel ligula facilisis gravida. Vivamus sit amet "
    "pellentesque arcu. Pellentesque habitant morbi tristique senectus "
    "et netus et malesuada fames ac turpis egestas.\n\n"

    "Párrafo 4:\n"
    "Etiam auctor, justo a tincidunt efficitur, risus sem fermentum "
    "est, id elementum est nibh a urna. Cras accumsan, mi ac suscipit "
    "lobortis, tellus odio consequat mi, in fermentum tortor mi sed nisl."
)

texto.insert("1.0", texto_largo)

root.mainloop()