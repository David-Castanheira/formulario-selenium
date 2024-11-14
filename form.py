import os 
import time 
from selenium import webdriver
from selenium.webdriver import Chrome 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

local_path = f'file://{os.path.dirname(os.path.realpath(__file__))}'

driver.get(f'{local_path}/templates/form.html')

nome = driver.find_element(By.NAME, "nome")
nome.send_keys('David')
time.sleep(0.8)

ra = driver.find_element(By.NAME, "ra")
ra.send_keys('2202571')
time.sleep(0.8)

dia = driver.find_element(By.ID, "dia")
dia.send_keys('05')
time.sleep(0.8)

mes = driver.find_element(By.ID, "mes")
mes.send_keys('Agosto')
time.sleep(0.8)

ano = driver.find_element(By.ID, "ano")
ano.send_keys('2003')
time.sleep(0.8)

ads = driver.find_element(By.ID, "ads")
ads.click()
time.sleep(0.8)

avaliacao = driver.find_element(By.ID, "avaliacao")
avaliacao.send_keys('9')
time.sleep(0.8)

sugestoes = driver.find_element(By.NAME, "sugestoes")
sugestoes.send_keys('Como forma de aumentar a dinâmica das aulas e o aprendizado, acredito que seria interessante reforçar os principais conceitos teóricos e tornar a aula mais prática')
time.sleep(0.8)

observacoes = driver.find_element(By.NAME, "observacoes")
observacoes.send_keys('Obrigado por nos acompanhar esse semestre, professor! Pude aprender algumas ferramentas ao longo para adicionar confiabilidade e segurança aos meus projetos. Saiba que será muito útil para o resto da minha carreira profissional.')
time.sleep(0.8)

botao_feedback = driver.find_element(By.XPATH, "//button[text()='Enviar feedback']")
botao_feedback.click()
time.sleep(0.8)
