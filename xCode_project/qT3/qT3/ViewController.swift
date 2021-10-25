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

    private func getData(from url: String, completion: @escaping (Result<MyResult, Error>) -> Void) {
        //var return_val: MyResult?
        
        let task = URLSession.shared.dataTask(with: URL(string: url)!,completionHandler: {data, response, error in
            guard let data = data, error == nil else {
                print(error)
                DispatchQueue.main.async {
                    completion(.failure(error as! Error))
                }
                return
            }
            //have data
            var result: MyResult?
            do{
                result = try JSONDecoder().decode(MyResult.self, from: data)
            }
            catch{
                print("failed to convert \(error.localizedDescription)")
                
            }
            guard let json = result else {
                return
            }
            
            
            print(json.word)
            print(json.form)
            
           DispatchQueue.main.async {
            completion(.success(json))
           }
           //return json
            //return_val = json.form
        })
        task.resume()
    
    }
    struct Response: Codable {
        let results: MyResult
        let status: String
    }
    struct MyResult: Codable{
        let word: String
        let form: String
       
        
    }

}



extension ViewController: UITextFieldDelegate{
    func textFieldShouldReturn(_ textField: UITextField) -> Bool {
        textField.resignFirstResponder()
        
        func updateLabel(input: String) -> Void{
            label.text = input
        }
        if let text = textField.text{
            label.text = text
            
            let verb_test: String
            let verb_encoded: String
            verb_test = text
            print(verb_test)
            verb_encoded = verb_test.addingPercentEncoding(withAllowedCharacters: .urlHostAllowed)!
            print(verb_encoded)
            let url = "https://qt3-arabic-deduction.herokuapp.com/api/form?id=" + verb_encoded
            //print(url)
            //var help = ""
            getData(from: url){ [self] results in
                
                //var test_help: String
                switch results {
                case .failure(let error):
                    print(error.localizedDescription)

                case .success(let response):
                    //print(response.form)
                    label.text = response.form
                    // use `genres` here, e.g. update model and UI
                }
                
            }
            
            //label.text = help
            
            
            //print("\(text)")
        }
        
        return true
    }
}
