import java.util.ArrayList;
import java.util.List;

public class Empregado {
  
  enum TipoEmpregado {MENSALISTA, HORISTA, AVULSO};

  int salarioMensal;
  double taxaEncargosTrabalhistas;
  int pagamentoPorHora;
  int horasTrabalhadas;
  int pagamentoAvulso;
  
  TipoEmpregado tipo;

  public static void main(String[] args) {
    List<Empregado> corpoDeTrabalho = new ArrayList<>();

    Empregado trabalhador1 = new Empregado();
    trabalhador1.salarioMensal = 5000;
    trabalhador1.taxaEncargosTrabalhistas = 1.8;
    trabalhador1.tipo = TipoEmpregado.MENSALISTA;
    corpoDeTrabalho.add(trabalhador1);

    Empregado trabalhador2 = new Empregado();
    trabalhador2.pagamentoPorHora = 150;
    trabalhador2.horasTrabalhadas = 30;
    trabalhador2.tipo = TipoEmpregado.HORISTA;
    corpoDeTrabalho.add(trabalhador2);

    Empregado trabalhador3 = new Empregado();
    trabalhador3.pagamentoAvulso = 7000;
    trabalhador3.tipo = TipoEmpregado.AVULSO;
    corpoDeTrabalho.add(trabalhador3);

    int custoTotal = 0;
    for (int i=0; i < 3; i++) {
      Empregado trabalhador = corpoDeTrabalho.get(i);

      switch (trabalhador.tipo) {
        case MENSALISTA:
          custoTotal += trabalhador.salarioMensal * 
                        trabalhador.taxaEncargosTrabalhistas;
          break;
        case HORISTA:
          custoTotal += trabalhador.pagamentoPorHora * 
                        trabalhador.horasTrabalhadas;
          break;
        case AVULSO:
          custoTotal += trabalhador.pagamentoAvulso;
      }
    }
    System.out.println("Minha folha de pagamento neste mês vai custar " + custoTotal);
  }

}
