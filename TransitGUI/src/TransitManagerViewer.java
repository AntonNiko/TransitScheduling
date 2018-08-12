
import java.awt.*;
import java.awt.event.*;
import java.awt.geom.AffineTransform;
import java.awt.geom.Point2D;
import java.awt.image.BufferedImage;
import java.beans.PropertyChangeListener;
import java.io.StringReader;
import java.net.URL;
import java.net.URLEncoder;
import java.text.NumberFormat;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedHashMap;
import java.util.logging.Level;
import java.util.logging.Logger;

import javax.swing.*;
import javax.swing.event.HyperlinkEvent;
import javax.swing.event.HyperlinkListener;
import javax.swing.text.html.HTMLDocument;
import javax.swing.text.html.HTMLEditorKit;
import javax.swing.text.html.StyleSheet;
import javax.xml.parsers.SAXParserFactory;

import org.xml.sax.Attributes;
import org.xml.sax.SAXException;
import org.xml.sax.helpers.DefaultHandler;


import java.awt.Component;
import javax.swing.*;
import static javax.swing.GroupLayout.Alignment.*;


public class TransitManagerViewer extends JFrame {
	JPanel headerPanel, helpPanel, tripPanel, toolsPanel;
	JTextField tripField;
	JButton tripSubmit;
	TripLoader loader;
	
	
    public TransitManagerViewer() {
    	setLayout(new GridLayout(2,2));
    	
    	
    	headerPanel = new JPanel();
    	tripField = new JTextField(5);
    	tripSubmit = new JButton("Load");
    	tripSubmit.addActionListener(new TripLoaderListener());
    	headerPanel.add(tripField);
    	headerPanel.add(tripSubmit);
    	
    	headerPanel.setBackground(Color.RED);
    	add(headerPanel);
    	
    	helpPanel = new JPanel();
    	helpPanel.setBackground(Color.YELLOW);
    	add(helpPanel);
    	
    	
    	tripPanel = new JPanel();
    	tripPanel.setBackground(Color.GREEN);
    	add(tripPanel);
    	
    	toolsPanel = new JPanel();
    	toolsPanel.setBackground(Color.BLUE);
    	add(toolsPanel);
    	
 
        setTitle("TransitViewer");
        pack();
        setSize(500, 300);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
    
    
    private class TripLoaderListener implements ActionListener
    {
    	public void actionPerformed(ActionEvent e)
    	{
    		TripLoader loader = new TripLoader(tripField.getText());
    	}
    }
    	
     
    public static void main(String args[]) {
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                try {
                    UIManager.setLookAndFeel(
                                  "javax.swing.plaf.metal.MetalLookAndFeel");
                                //  "com.sun.java.swing.plaf.motif.MotifLookAndFeel");
                                //UIManager.getCrossPlatformLookAndFeelClassName());
                } catch (Exception ex) {
                    ex.printStackTrace();
                }
                new TransitManagerViewer().setVisible(true);
            }
        });
    }
}

