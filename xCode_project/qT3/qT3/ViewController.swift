//
//  ViewController.swift
//  qT3
//
//  Created by Sabrina Templeton on 10/10/21.
//

import UIKit

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        let listReturn:Array<String> = randomReturn(str: "Hello World!")
        var count:Int = 0
        for item in listReturn{
            let button: UIButton = UIButton()
            button.setTitle(item, for: .normal)
            button.tag = count
            button.setTitleColor(.blue, for: .normal)
            button.frame = CGRect(x: 20, y: 100 * count, width: 200, height: 40)
            count += 1
            button.addTarget(self, action: #selector(onTap(sender:)), for: .touchUpInside)
            view.addSubview(button)
            
        

          
        }
        
       

    }
    
    @objc func onTap(sender: UIButton) {
        print("tapped")
        let story = UIStoryboard(name: "Main", bundle: nil)
        let controller = story.instantiateViewController(identifier: "SecondController") as! SecondController
       // self.present(controller, animated: true, completion: nil)
        let navigation = UINavigationController(rootViewController: controller)
        self.view.addSubview(navigation.view)
        let label = UILabel(frame: CGRect(x: 100, y: 300, width: 200, height: 40))
        label.text = String(sender.tag)
        self.view.addSubview(label)
        self.addChild(navigation)
        navigation.didMove(toParent: self)
        
    }

    
    


}

func randomReturn(str: String) -> Array<String> {
    var returnVar: [String] = []
    for char in str{
        returnVar.append(String(char))
    }
    return returnVar
}
