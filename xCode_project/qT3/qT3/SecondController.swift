//
//  SecondController.swift
//  qT3
//
//  Created by Sabrina Templeton on 12/6/21.
//

import UIKit

class SecondController: UIViewController {

    var formLabel: UILabel!
    var rectangleView: UIView!
    var formTitle: UILabel!
    var rootLabel: UILabel!
    var rootTitle: UILabel!
    var rectangleView1: UIView!
    var infoLabel: UITextView!
    var infoTitle: UILabel!
    var rectangleView2: UIView!
    var globalResults:MyResults?
    
//    @IBOutlet his class is not key value coding-compliant for the key button.'
//    @IBOutlet var button: UIButton!
 
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        view.backgroundColor = .systemGray
        title = "qT3"
//        field.returnKeyType = .done
//        field.autocorrectionType = .no
//        field.becomeFirstResponder()
//        field.delegate = self
//
       
        formTitle = UILabel(frame: CGRect(x: 40, y: 175, width: 200, height: 50))
        formTitle.text = "form:"
        formTitle.font = UIFont.boldSystemFont(ofSize: 16)
        rectangleView = UIView(frame: CGRect(x: 0, y: 200, width: 300, height: 50))
        rectangleView.backgroundColor = .systemBlue
        rectangleView.alpha = 0.5
        
      
        rootTitle = UILabel(frame: CGRect(x: 200, y: 275, width: 200, height: 50))
        rootTitle.text = "root:"
        rootTitle.font = UIFont.boldSystemFont(ofSize: 16)
        rectangleView1 = UIView(frame: CGRect(x: 200, y: 300, width: 300, height: 50))
        rectangleView1.backgroundColor = .systemBlue
        rectangleView1.alpha = 0.5
        
       
        infoTitle = UILabel(frame: CGRect(x: 40, y: 375, width: 200, height: 50))
        infoTitle.text = "info:"
        infoTitle.font = UIFont.boldSystemFont(ofSize: 16)
        rectangleView2 = UIView(frame: CGRect(x: 0, y: 400, width: 400, height: 200))
        rectangleView2.backgroundColor = .systemBlue
        //rectangleView2.alpha = 0.5

        
        view.addSubview(rectangleView)
        view.addSubview(formTitle)
        //view.addSubview(formLabel)
        view.addSubview(rectangleView1)
        view.addSubview(rootTitle)
        //view.addSubview(rootLabel)
        view.addSubview(rectangleView2)
        view.addSubview(infoTitle)
        //view.addSubview(infoLabel)
        configureButtons()
        
      
    }
    private func configureButtons(){
        navigationItem.leftBarButtonItem = UIBarButtonItem(barButtonSystemItem: .rewind, target: self, action: #selector(onTapBack))
    }
    
    @objc func onTapBack() {
        print("tapped")
        let story = UIStoryboard(name: "Main", bundle: nil)
        let controller = story.instantiateViewController(identifier: "FirstController") as! ViewController
        self.present(controller, animated: true, completion: nil)
        //let navigation = UINavigationController(rootViewController: controller)
        //self.view.addSubview(navigation.view)
      
        //self.view.addSubview(label)
//        self.addChild(navigation)
//        navigation.didMove(toParent: self)
        
    }
    
//    @IBAction func buttonTapped(){
//        //field.resignFirstResponder()
//        print("button tapped")
//    }

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
            
            
            print(json)
            
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
        let input: String
        let word: String
        let form: String
        let features: Array<Feature>
        let root: String
        let weak: Bool
        
       
        
    }
    struct MyResults: Codable{
        let possible_words: Array<MyResult>
    }
     

}



//extension SecondController: UITextFieldDelegate{
//    func textFieldShouldReturn(_ textField: UITextField) -> Bool {
//        textField.resignFirstResponder()
//
//        func updateLabel(input: String) -> Void{
//            formLabel.text = input
//        }
//        if let text = textField.text{
//            formLabel.text = text
//
//            let verb_test: String
//            let verb_encoded: String
//            verb_test = text
//            print(verb_test)
//            verb_encoded = verb_test.addingPercentEncoding(withAllowedCharacters: .urlHostAllowed)!
//            print(verb_encoded)
//            let url = "http://127.0.0.1:5000/api/verb?id=" + verb_encoded
//            //let url = "https://qt3-arabic-deduction.herokuapp.com/api/verb?id=" + verb_encoded
//
//
//            getData(from: url){ [self] results in
//
//                //var test_help: String
//                switch results {
//                case .failure(let error):
//                    print(error.localizedDescription)
//
//                case .success(let response):
//                    //print(response.form)
//                   // var featureStringMonster = " "
//                    let word = response.possible_words[0]
//                    var genders = "gender: "
//                    var tenses = "tense: "
//                    var moods = "mood: "
//                    var nums = "number: "
//                    var persons = "person: "
//
//                    for feature in response.features{
//                        genders = genders + " " + feature.gender
//                        tenses = tenses + " " + feature.tense
//                        moods = moods + " " + feature.mood
//                        nums = nums + " " + String(feature.number)
//                        persons = persons + " " + String(feature.person)
////                        print(feature)
////                        let tenseNum = feature.tense + " " + String(feature.number) + " "
////
////                        let personGender = feature.gender + " " + String(feature.person) + " "
////                        let mood = feature.mood + "\n"
////                        let featureString = tenseNum + personGender + mood
////                        featureStringMonster = featureStringMonster + featureString
//                        //feature
//
//                    }
//                    formLabel.text = response.form //+ " " + response.root + "\n" + featureStringMonster
//                    rootLabel.text = response.root
//
//                    infoLabel.text = genders + "\n" + tenses + "\n" + moods + "\n" + nums + "\n" + persons
//                    // use `genres` here, e.g. update model and UI
//                }
//
//            }
//
//            //label.text = help
//
//
//            //print("\(text)")
//        }
//
//        return true
//    }
//}
