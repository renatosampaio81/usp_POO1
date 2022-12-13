package polimorfismo.OO_polimorfismo;

public class EmpregadoAvulso extends Empregado {

	private int pagamento;
	
	EmpregadoAvulso(int valor) {
		pagamento = valor;
	}
	
	int pagamentoDoMes() {
		return pagamento;
	}

	public String toString() {
		return "Sou um empregado avulso e cobrei R$"+ pagamento;
	}
}
