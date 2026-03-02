from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Cliente(Base):
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100))
    telefone = Column(String(20))


class Material(Base):
    __tablename__ = "materiais"
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    custo_unitario = Column(Numeric(10, 2), nullable=False)
    unidade_medida = Column(String(20), nullable=False)


class Produto(Base):
    __tablename__ = "produtos"
    id = Column(Integer,primary_key=True)
    nome = Column(String(100), nullable=False)
    margem_lucro_percentual = Column(Numeric(5, 2), nullable=False)


class Producao(Base):
    __tablename__ = "producoes"
    id = Column(Integer, primary_key=True)
    produto_id = Column(Integer, ForeignKey("produtos.id"), nullable=False)
    quantidade_produzida = Column(Integer, nullable=False)
    custo_total = Column(Numeric(10, 2))
    preco_sugerido = Column(Numeric(10, 2))


class ProducaoMaterial(Base):
    __tablename__ = "producao_materiais"
    id = Column(Integer, primary_key=True)
    producao_id = Column(Integer, ForeignKey("producoes.id"), nullable=False)
    material_id = Column(Integer, ForeignKey("materiais.id"), nullable=False)
    quantidade_utilizada = Column(Numeric(10, 2), nullable=False)
    custo_calculado = Column(Numeric(10, 2))