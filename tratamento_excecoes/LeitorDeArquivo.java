package tratamento_excecoes;
import java.io.FileReader;

public class LeitorDeArquivo {
  
  static char [] leArquivo (String nomeArq) {
    char [] conteudo = new char[1024];
    try {
    	if (nomeArq.endsWith(".c"))  // Se a extensão do arquivo carregado for .c
    		throw new UglyFileException();  // Lanća a extensão UglyFlieException
    	FileReader fr = new FileReader(nomeArq);
    	fr.read(conteudo);
    	fr.close();
    }
    catch (Exception e) {
      System.out.println("Não consegui abrir o arquivo : " + e);
    }
    return conteudo;
  }

  public static void main (String[] args) {
    try {
      System.out.println(leArquivo(args[0]));
    }
    catch (Exception e) {
      System.out.println("Erro ao imprimir arquivo na tela : " + e);
    }
    
  }

}
