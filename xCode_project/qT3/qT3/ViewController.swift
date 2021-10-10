//
//  ViewController.swift
//  qT3
//
//  Created by Sabrina Templeton on 10/10/21.
//

import UIKit

class ViewController: UIViewController {
    
    var label: UILabel!
    
    @IBOutlet var field: UITextField!
    @IBOutlet var button: UIButton!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        view.backgroundColor = .systemGray
        field.returnKeyType = .done
        field.autocorrectionType = .no
        field.becomeFirstResponder()
        field.delegate = self
        
        label = UILabel(frame: CGRect(x: 100, y: 200, width: 220, height: 50))
        label.text = "text"
        view.addSubview(label)
    }
    
    @IBAction func buttonTapped(){
        field.resignFirstResponder()
    }


}

extension ViewController: UITextFieldDelegate{
    func textFieldShouldReturn(_ textField: UITextField) -> Bool {
        textField.resignFirstResponder()
        
        if let text = textField.text{
            label.text = text
            print("\(text)")
        }
        
        return true
    }
}
