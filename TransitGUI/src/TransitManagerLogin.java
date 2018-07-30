
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


public class TransitManagerLogin extends JFrame {
    public TransitManagerLogin() {
        JLabel usernameLabel = new JLabel("Username:");
        JLabel passwordLabel = new JLabel("Password:");
        JTextField usernameField = new JTextField();
        JPasswordField passwordField = new JPasswordField();
        JButton loginButton = new JButton("Login");
        JButton cancelButton = new JButton("Cancel");
        
        
        // ActionListeners
        loginButton.addActionListener(new ActionListener()
        {
        	public void actionPerformed(ActionEvent e)
        	{
        		// Authenticate user
        		System.out.println(usernameField.getText());
        		System.out.println(passwordField.getPassword());
        	}
   		});
        
        // remove redundant default border of check boxes - they would hinder
        // correct spacing and aligning (maybe not needed on some look and feels)
        GroupLayout layout = new GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setAutoCreateGaps(true);
        layout.setAutoCreateContainerGaps(true);
 
        layout.setHorizontalGroup(layout.createSequentialGroup()
            .addGroup(layout.createParallelGroup(LEADING)
                    .addComponent(usernameLabel)
                    .addComponent(passwordLabel)	
            		)
            .addGroup(layout.createParallelGroup(LEADING)
                .addComponent(usernameField)
                .addComponent(passwordField)
                .addGroup(layout.createSequentialGroup()
                    .addGroup(layout.createParallelGroup(LEADING))
                    	
                    .addGroup(layout.createParallelGroup(LEADING)
                        )))
            .addGroup(layout.createParallelGroup(LEADING)
                .addComponent(loginButton))
        );
        
        layout.linkSize(SwingConstants.HORIZONTAL, loginButton);
 
        layout.setVerticalGroup(layout.createSequentialGroup()
            
        	.addGroup(layout.createParallelGroup(BASELINE)
                .addComponent(usernameLabel)
                .addComponent(usernameField)
                
                .addComponent(loginButton))
            .addGroup(layout.createParallelGroup(LEADING)
                .addGroup(layout.createSequentialGroup()
                    .addGroup(layout.createParallelGroup(BASELINE)
                    	.addComponent(passwordLabel)
                    	.addComponent(passwordField))
                    .addGroup(layout.createParallelGroup(BASELINE)))
                )
        );
 
        setTitle("TransitManager");
        pack();
        setSize(500, 800);
        setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
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
                new TransitManagerLogin().setVisible(true);
            }
        });
    }
}

