package org.cards;

import com.opencsv.CSVParser;
import com.opencsv.CSVParserBuilder;
import com.opencsv.CSVReader;
import com.opencsv.CSVReaderBuilder;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public class App
{
    public static void main( String[] args )
    {
        try {
            CSVParser parser = new CSVParserBuilder().withSeparator('|')
                                                     .withIgnoreQuotations(true)
                                                     .build();
            CSVReader reader = new CSVReaderBuilder(new FileReader("src/main/resources/CK_PRICES_11122021.txt"))
                    .withSkipLines(1).withCSVParser(parser).build();
            //CSVReader reader = new CSVReader(new FileReader("src/main/resources/CK_PRICES_11122021.txt"),'|','"',0);
            List<String[]> cards = reader.readAll();
            System.out.println( reader.getRecordsRead());
            System.out.println(cards.get(0)[1]);
            Collections.sort(cards, new Comparator<String[]>() {
                @Override
                public int compare(String[] o1, String[] o2) {
                    return o1[1].compareTo(o2[1]);
                }
            });
            System.out.println(cards.get(0)[1]);

            reader.close();

        }
        catch (Exception fnfe) {
            fnfe.printStackTrace();
        }
    }
}
