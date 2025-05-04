import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Dashboard-Klasse, die die GUI für das Dashboard erstellt
class Dashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Studiengang Dashboard")  # Setzt den Titel des Dashboards

        # STUDIENGANG Bereich (links)
        self.frame_studiengang = tk.LabelFrame(self.root, text="STUDIENGANG", padx=10, pady=10)
        self.frame_studiengang.grid(row=0, column=0, padx=10, pady=10)

        # Erreichte ECTS Eingabe
        self.label_ects = tk.Label(self.frame_studiengang, text="Erreichte ECTS:")
        self.label_ects.grid(row=0, column=0, sticky="w")  # Positionierung des Labels
        self.entry_ects = tk.Entry(self.frame_studiengang)
        self.entry_ects.grid(row=0, column=1)  # Positionierung des Eingabefelds

        # Progressbar für Studienfortschritt (Visualisiert den Studienfortschritt)
        self.progress = ttk.Progressbar(self.frame_studiengang, length=200, mode="determinate", maximum=180, value=60)
        self.progress.grid(row=1, column=0, columnspan=2)

        # Text zur Anzeige des Studienfortschritts
        self.progress_text = tk.Label(self.frame_studiengang, text="33%", font=("Helvetica", 12))
        self.progress_text.grid(row=2, column=0, columnspan=2)

        # Speichern und Zurücksetzen Buttons für den Studiengang
        self.btn_speichern_studiengang = tk.Button(self.frame_studiengang, text="Speichern", command=self.speichern_studiengang)
        self.btn_speichern_studiengang.grid(row=3, column=0)
        self.btn_reset_studiengang = tk.Button(self.frame_studiengang, text="Zurücksetzen", command=self.reset_studiengang)
        self.btn_reset_studiengang.grid(row=3, column=1)

        # NOTENSCHNITT Bereich (Mitte)
        self.frame_notenschnitt = tk.LabelFrame(self.root, text="Notenschnitt", padx=10, pady=10)
        self.frame_notenschnitt.grid(row=0, column=1, padx=10, pady=10)

        # Noten Eingabefelder
        self.label_note1 = tk.Label(self.frame_notenschnitt, text="Note Nummer 1:")
        self.label_note1.grid(row=0, column=0, sticky="w")
        self.entry_note1 = tk.Entry(self.frame_notenschnitt)
        self.entry_note1.grid(row=0, column=1)

        self.label_note2 = tk.Label(self.frame_notenschnitt, text="Note Nummer 2:")
        self.label_note2.grid(row=1, column=0, sticky="w")
        self.entry_note2 = tk.Entry(self.frame_notenschnitt)
        self.entry_note2.grid(row=1, column=1)

        self.label_note3 = tk.Label(self.frame_notenschnitt, text="Note Nummer 3:")
        self.label_note3.grid(row=2, column=0, sticky="w")
        self.entry_note3 = tk.Entry(self.frame_notenschnitt)
        self.entry_note3.grid(row=2, column=1)

        # Notenschnitt Berechnung und Anzeige
        self.label_notenschnitt = tk.Label(self.frame_notenschnitt, text="Notenschnitt:")
        self.label_notenschnitt.grid(row=3, column=0, sticky="w")
        self.notenschnitt_label = tk.Label(self.frame_notenschnitt, text="Ø", font=("Helvetica", 12))
        self.notenschnitt_label.grid(row=3, column=1)

        # Speichern und Zurücksetzen Buttons für den Notenschnitt
        self.btn_speichern_notenschnitt = tk.Button(self.frame_notenschnitt, text="Speichern", command=self.speichern_notenschnitt)
        self.btn_speichern_notenschnitt.grid(row=4, column=0)
        self.btn_reset_notenschnitt = tk.Button(self.frame_notenschnitt, text="Zurücksetzen", command=self.reset_notenschnitt)
        self.btn_reset_notenschnitt.grid(row=4, column=1)

        # LERNVERLAUF Bereich (rechts)
        self.frame_lernverlauf = tk.LabelFrame(self.root, text="Lernverlauf", padx=10, pady=10)
        self.frame_lernverlauf.grid(row=0, column=2, padx=10, pady=10)

        # Lernstunden Eingabe
        self.label_lernstunden = tk.Label(self.frame_lernverlauf, text="Lernstunden:", font=("Helvetica", 12))
        self.label_lernstunden.grid(row=0, column=0, sticky="w")
        self.entry_lernstunden = tk.Entry(self.frame_lernverlauf)
        self.entry_lernstunden.grid(row=0, column=1)

        # Lernverlauf Diagramm (Matplotlib)
        self.plot_figure = plt.Figure(figsize=(5, 3), dpi=100)
        self.plot_ax = self.plot_figure.add_subplot(111)
        weeks = list(range(1, 17))  # Kalenderwochen 1 bis 16
        learning_hours = [6, 7, 5, 6, 8, 7, 6, 5, 6, 7, 8, 9, 10, 8, 9, 10]  # Beispiel-Lernstunden pro Woche
        self.plot_ax.plot(weeks, learning_hours, marker='o')

        # Diagrammtitel und Achsenbeschriftungen
        self.plot_ax.set_title("Lernstunden pro Woche")
        self.plot_ax.set_xlabel("KW")
        self.plot_ax.set_ylabel("Lernstunden")

        # Matplotlib Canvas einfügen
        self.canvas = FigureCanvasTkAgg(self.plot_figure, master=self.frame_lernverlauf)
        self.canvas.get_tk_widget().grid(row=1, column=0, columnspan=2)

        # Speichern und Zurücksetzen Buttons für den Lernverlauf
        self.btn_speichern_lernverlauf = tk.Button(self.frame_lernverlauf, text="Speichern", command=self.speichern_lernverlauf)
        self.btn_speichern_lernverlauf.grid(row=2, column=0)
        self.btn_reset_lernverlauf = tk.Button(self.frame_lernverlauf, text="Zurücksetzen", command=self.reset_lernverlauf)
        self.btn_reset_lernverlauf.grid(row=2, column=1)

    # Funktionen zum Speichern der Daten und Zurücksetzen der Felder

    def speichern_studiengang(self):
        # Studiengang (ECTS) speichern
        try:
            ects = int(self.entry_ects.get())
            progress = (ects / 180) * 100  # Berechnung des Studienfortschritts in Prozent
            self.progress['value'] = progress
            self.progress_text.config(text=f"{progress:.1f}% ({ects} ECTS)")  # Anzeige des Fortschritts
        except ValueError:
            messagebox.showerror("Fehler", "Bitte eine gültige Zahl für ECTS eingeben.")

    def reset_studiengang(self):
        # Zurücksetzen des Studienfortschritts
        self.entry_ects.delete(0, tk.END)
        self.progress['value'] = 0
        self.progress_text.config(text="0% (0 ECTS)")

    def speichern_notenschnitt(self):
        # Noten speichern und Notenschnitt berechnen
        try:
            note1 = float(self.entry_note1.get())
            note2 = float(self.entry_note2.get())
            note3 = float(self.entry_note3.get())
            notenschnitt = (note1 + note2 + note3) / 3
            self.notenschnitt_label.config(text=f"{notenschnitt:.2f}")  # Anzeige des Notenschnitts
        except ValueError:
            messagebox.showerror("Fehler", "Bitte gültige Noten eingeben.")

    def reset_notenschnitt(self):
        # Zurücksetzen der Noten und des Notenschnitts
        self.entry_note1.delete(0, tk.END)
        self.entry_note2.delete(0, tk.END)
        self.entry_note3.delete(0, tk.END)
        self.notenschnitt_label.config(text="Ø")

    def speichern_lernverlauf(self):
        # Lernstunden speichern (Hier könnte man z.B. auch die Daten zur späteren Verwendung speichern)
        try:
            lernstunden = float(self.entry_lernstunden.get())
            print(f"Lernstunden gespeichert: {lernstunden}")  # Hier könnten die Daten gespeichert werden
        except ValueError:
            messagebox.showerror("Fehler", "Bitte eine gültige Zahl für Lernstunden eingeben.")

    def reset_lernverlauf(self):
        # Zurücksetzen der Lernstunden
        self.entry_lernstunden.delete(0, tk.END)

# Hauptprogramm starten
if __name__ == "__main__":
    root = tk.Tk()  # Erstellen des Hauptfensters
    dashboard = Dashboard(root)  # Erstellen des Dashboard-Objekts
    root.mainloop()  # Starten der GUI