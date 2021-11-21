import java.io.File;
import java.io.IOException;
import java.util.Scanner;
import java.util.Calendar;
import java.text.SimpleDateFormat;

public class file_sort {

    private static String now(){
        Calendar cal = Calendar.getInstance();
        SimpleDateFormat date_today = new SimpleDateFormat("ddMMYYYY");
        return date_today.format(cal.getTime());
    }

    private static void parseData(String str){
        String id, name, type, set, rarity, nm, ex, vg, g, card_text;
        Scanner lineScanner = new Scanner(str);
        lineScanner.useDelimiter("\\|");
        while(lineScanner.hasNext()){
            id = lineScanner.next();
            name = lineScanner.next();
            type = lineScanner.next();
            set = lineScanner.next();
            rarity = lineScanner.next();
            nm = lineScanner.next();
            ex = lineScanner.next();
            vg = lineScanner.next();
            g = lineScanner.next();
            card_text = lineScanner.next();
            System.out.println("Name: " + name + ", Type: " + type + ", Set: " + set + ", Rarity"
                                + rarity + ", NM: " + nm + ", EX: " + ex + ", VG: " + vg + ", G: "
                                + g + ", Card Text: " + card_text);  
          }
          lineScanner.close();
    }

    public static void main(String[] args){
        Scanner sc = null;
        String date = now();
        String currentDir = System.getProperty("user.dir");
        try{
            sc = new Scanner( new File(currentDir + "\\Card_Kingdom\\" + date + "\\" + "CK_PRICES_" + date + ".txt"));
            while(sc.hasNextLine()){
                String str = sc.nextLine();
                parseData(str);
            }
        } catch (IOException ioe){
            ioe.printStackTrace();
        }finally{
            if(sc != null ){
                sc.close();
            }
        }
    }
}