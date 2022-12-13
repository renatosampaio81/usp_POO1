package polimorfismo.OO_polimorfismo;

public class EmpregadoHorista extends Empregado {

	private int salarioPorHora;
	private int horasTrabalhadas;
	
	EmpregadoHorista(int salarioPorHora, int horas) {
		this.salarioPorHora = salarioPorHora;
		this.horasTrabalhadas = horas;
	}

	int pagamentoDoMes() {
		return salarioPorHora * horasTrabalhadas;
	}

	public String toString() {
		return "Sou um empregado horista, ganho R$"+ salarioPorHora +
				" e trabalhei " + horasTrabalhadas + " horas / ";
	}
}