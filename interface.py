# interface.py
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from processamento import processar_excel
import pandas as pd

def selecionar_arquivo():
    caminho_arquivo = filedialog.askopenfilename(filetypes=[("Arquivos Excel", "*.xlsx")])
    
    if not caminho_arquivo.endswith('.xlsx'):
        messagebox.showerror("Erro", "Por favor, selecione um arquivo Excel válido.")
        return
    
    if caminho_arquivo:
        try:
            dados_cruzados = processar_excel(caminho_arquivo)
            resultado_text.delete(1.0, tk.END)
            resultado_text.insert(tk.END, dados_cruzados.to_string())
            dados_cruzados.to_excel('dados_cruzados.xlsx', index=False)
            messagebox.showinfo("Sucesso", "Dados processados e salvos em 'dados_cruzados.xlsx'.")
        
        except FileNotFoundError:
            messagebox.showerror("Erro", "Arquivo não encontrado.")
        except pd.errors.ExcelFileError as e:
            messagebox.showerror("Erro no Excel", f"Erro ao ler o arquivo Excel: {e}")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

root = tk.Tk()
root.title("Processador de Arquivos Excel")

root.geometry("700x500")

root.protocol("WM_DELETE_WINDOW", root.quit)

btn_selecionar = ttk.Button(root, text="Selecionar Arquivo Excel", command=selecionar_arquivo)
btn_selecionar.pack(pady=10)

scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

resultado_text = tk.Text(root, height=15, width=70, yscrollcommand=scrollbar.set)
resultado_text.pack(pady=20)

scrollbar.config(command=resultado_text.yview)

root.mainloop()
