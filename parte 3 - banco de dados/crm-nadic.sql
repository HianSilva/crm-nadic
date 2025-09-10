-- Tabela de clientes
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    phone VARCHAR(20) NOT NULL
);

-- Tabela de produtos
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(500) NOT NULL,
    price NUMERIC(10,2) NOT NULL,
    stock_quantity INT NOT NULL
);

ALTER TABLE products ADD CONSTRAINT chk_price_positive CHECK (price > 0);

-- Tabela de pedidos
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    customer_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE CASCADE
);

-- Tabela de itens do pedido
CREATE TABLE order_items (
    id SERIAL PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    quantity INT NOT NULL,
    product_sale_price NUMERIC(10,2) NOT NULL,
    total_price NUMERIC(10,2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(id)
);

ALTER TABLE order_items ADD CONSTRAINT chk_quantity_positive CHECK (quantity > 0);

-- Tabela de receita
CREATE TABLE revenue (
    id SERIAL PRIMARY KEY,
    value NUMERIC(15,2) NOT NULL,
    year INT NOT NULL,
    month VARCHAR(20),
    trimester INTEGER,
    semester INTEGER,
    time_period VARCHAR(30),
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Inserindo clientes
INSERT INTO customers (name, email, phone) VALUES
('João Silva', 'joao.silva@email.com', '11999990001'),
('Maria Oliveira', 'maria.oliveira@email.com', '11999990002'),
('Carlos Souza', 'carlos.souza@email.com', '11999990003'),
('Ana Lima', 'ana.lima@email.com', '11999990004'),
('Bruno Costa', 'bruno.costa@email.com', '11999990005'),
('Fernanda Torres', 'fernanda.torres@email.com', '11999990006'),
('Pedro Mendes', 'pedro.mendes@email.com', '11999990007'),
('Juliana Martins', 'juliana.martins@email.com', '11999990008'),
('Lucas Rocha', 'lucas.rocha@email.com', '11999990009'),
('Patricia Ramos', 'patricia.ramos@email.com', '11999990010');

-- Inserindo produtos (SEM category)
INSERT INTO products (name, price, stock_quantity) VALUES
('Notebook Dell', 3500.00, 15),
('Mouse Logitech', 120.00, 100),
('Teclado Mecânico', 350.00, 40),
('Monitor LG 24"', 850.00, 25),
('Impressora HP', 900.00, 20),
('Smartphone Samsung', 2100.00, 30),
('Fone JBL', 250.00, 80),
('HD Externo', 400.00, 50),
('SSD Kingston 480GB', 320.00, 60),
('Webcam Logitech', 200.00, 45);

-- Inserindo pedidos (SEM status)
INSERT INTO orders (customer_id) VALUES
(1),
(2),
(3),
(4),
(5),
(6),
(7),
(8),
(9),
(10),
(1),
(2),
(3),
(4),
(5);

-- Inserindo itens dos pedidos
INSERT INTO order_items (order_id, product_id, quantity, product_sale_price, total_price) VALUES
(1, 1, 1, 3500.00, 3500.00),
(1, 2, 2, 120.00, 240.00),
(2, 3, 1, 350.00, 350.00),
(2, 4, 1, 850.00, 850.00),
(3, 5, 1, 900.00, 900.00),
(4, 6, 1, 2100.00, 2100.00),
(4, 7, 2, 250.00, 500.00),
(5, 8, 1, 400.00, 400.00),
(5, 9, 1, 320.00, 320.00),
(6, 2, 3, 120.00, 360.00),
(7, 10, 1, 200.00, 200.00),
(8, 1, 1, 3500.00, 3500.00),
(9, 5, 2, 900.00, 1800.00),
(10, 8, 1, 400.00, 400.00),
(11, 3, 1, 350.00, 350.00),
(12, 4, 2, 850.00, 1700.00),
(13, 6, 1, 2100.00, 2100.00),
(14, 9, 2, 320.00, 640.00),
(15, 7, 1, 250.00, 250.00);