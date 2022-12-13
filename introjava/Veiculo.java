
public class Veiculo {
	private int anoDeFabricacao;
	private String modelo;
	private String marca;
	
	Veiculo (int adf, String m, String ma) {
		anoDeFabricacao = adf;
		modelo = m;
		marca = ma;
	}

	public int getAnoDeFabricacao() {
		return anoDeFabricacao;
	}

	public void setAnoDeFabricacao(int anoDeFabricacao) {
		this.anoDeFabricacao = anoDeFabricacao;
	}
}
