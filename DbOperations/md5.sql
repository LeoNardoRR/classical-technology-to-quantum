use aes;
select * from ic;
select nome, aes_decrypt(senha, 'senha') as SenhaD from ic;

