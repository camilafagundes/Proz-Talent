const titulo = document.createElement("h1");
titulo.id = "titulo";
titulo.innerText = "Bem-vindo à nossa Loja Virtual!";
document.body.appendChild(titulo);

const produto = document.createElement("div");
produto.classList.add("produto");

const nome = document.createElement("h2");
nome.innerText = "Camiseta Estilosa";

const descricao = document.createElement("p");
descricao.innerText = "Camiseta 100% algodão, confortável e moderna.";

const preco = document.createElement("p");
preco.innerText = "Preço: R$ 59,90";

const imagem = document.createElement("img");
imagem.src = "https://via.placeholder.com/150";
imagem.alt = "Imagem da camiseta";
imagem.style.width = "150px";

produto.appendChild(nome);
produto.appendChild(descricao);
produto.appendChild(preco);
produto.appendChild(imagem);

document.body.appendChild(produto);
