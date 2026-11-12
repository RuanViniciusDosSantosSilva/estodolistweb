INSERT INTO tarefa (nomeTarefa, descricao, categoria, dataPrazo, prioridade, status)
VALUES
('Trabalho de História',
'Capítulo 4 e resumo de 2 páginas',
'Escola', '2026-12-10', 'ALTA', 'Pendente'),

('Prova de BD',
'Revisar JOINs e normalização',
'Faculdade', '2026-11-25', 'ALTA', 'Pendente'),

('Compras do mês',
'Arroz, feijão, café e limpeza',
'Casa', '2026-11-20', 'MEDIA', 'Pendente'),

('Relatório semanal',
'Enviar para o supervisor',
'Trabalho', '2026-11-18', 'MEDIA', 'Pendente'),

('Consulta no dentista',
'Ligar e agendar limpeza',
'Pessoal', '2026-12-05', 'MEDIA', 'Pendente');

SELECT * FROM tarefa;