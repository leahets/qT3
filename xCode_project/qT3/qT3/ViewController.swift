//
//  ViewController.swift
//  qT3
//
//  Created by Sabrina Templeton on 10/10/21.
//

import UIKit

class ViewController: UIViewController {
    
    var formLabel: UILabel!
    var formSubmit: UIButton!

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        let listReturn:Array<String> = randomReturn(str: "Help")
        var count:Int = 1
        for item in listReturn{
            let button: UIButton = UIButton()
            button.setTitle(item, for: .normal)
            button.tag = count
            button.setTitleColor(.blue, for: .normal)
            button.frame = CGRect(x: 20, y: 100 + 100 * count, width: 200, height: 40)
            count += 1
            button.addTarget(self, action: #selector(onTap(sender:)), for: .touchUpInside)
            view.addSubview(button)
            
        

          
        }
        
        formLabel = UILabel(frame: CGRect(x: 20, y: 400, width: 100, height: 40))
        //formLabel.backgroundColor = .systemBlue
        var userField = UITextField(frame: CGRect(x: 20, y: 100, width: 300, height: 40))
        userField.backgroundColor = .systemBlue
        userField.alpha = 0.5
        userField.returnKeyType = .done
        userField.becomeFirstResponder()
        userField.delegate = self
        userField.autocorrectionType = .no
        //var formSubmit = UIButton(frame: CGRect(x: 20, y:160, width: 80, height: 40))
        //formSubmit.setTitle("Deduct!", for: .normal)
        
        view.addSubview(userField)
        view.addSubview(formLabel)
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

private func getData(from url: String, completion: @escaping (Result<MyResults, Error>) -> Void) {
    //var return_val: MyResult?
    
    let task = URLSession.shared.dataTask(with: URL(string: url)!,completionHandler: {data, response, error in
        guard let data = data, error == nil else {
            print(error ?? "unknown error")
            DispatchQueue.main.async {
                completion(.failure(error!))
            }
            return
        }
        //have data
        var result: MyResults?
        do{
            result = try JSONDecoder().decode(MyResults.self, from: data)
        }
        catch{
            print("failed to convert \(error.localizedDescription)")
            
        }
        guard let json = result else {
            return
        }
        
        
        print(json.possible_words[0])
        print(json.possible_words[0].form)
        
       DispatchQueue.main.async {
        completion(.success(json))
       }
       //return json
        //return_val = json.form
    })
    task.resume()

}
struct Feature: Codable {
    let tense: String
    let number: Int
    let gender: String
    let person: Int
    let mood: String

}
struct MyResult: Codable{
    let word: String
    let form: String
    let features: Array<Feature>
    let root: String
    
}
struct MyResults: Codable{
    let possible_words: Array<MyResult>
}


 


extension ViewController: UITextFieldDelegate{
    func textFieldShouldReturn(_ textField: UITextField) -> Bool {
        textField.resignFirstResponder()
        
        //let text = textField.text
        //formLabel.text = text
//        func updateLabel(input: String) -> Void{
//            formLabel.text = input
//        }
//        return true
//    }
//}
       if let text = textField.text{
            formLabel.text = text
            
            let verb_test: String
            let verb_encoded: String
            verb_test = text
            print(verb_test)
            verb_encoded = verb_test.addingPercentEncoding(withAllowedCharacters: .urlHostAllowed)!
            print(verb_encoded)
            let url = "https://qt3-arabic-deduction.herokuapp.com/api/verb?id=" + verb_encoded
            
            
            getData(from: url){ [self] results in
                
                //var test_help: String
                switch results {
                case .failure(let error):
                    print(error.localizedDescription)

                case .success(let response):
                    print (response)
       
                }
                
            }
            
            //label.text = help
            
            
            //print("\(text)")
        }
        
        return true
    }
}
//*/
