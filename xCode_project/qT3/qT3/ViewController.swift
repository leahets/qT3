//
//  ViewController.swift
//  qT3
//
//  Created by Sabrina Templeton on 10/10/21.
//

import UIKit

class CurrentWords: ObservableObject{
    @Published var currWords:Int = 0

}

class ViewController: UIViewController {
    //@StateObject var global_results = CurrrentWords()
    var globalResults = CurrentWords()
    var localResults: MyResults?
    var currentWord: MyResult?
    
    var formLabel: UILabel!
    var formSubmit: UIButton!
    
    //var globalResults: MyResults?

    override func viewDidLoad() {
        super.viewDidLoad()
        let screenWidth = self.view.frame.size.width

        //formLabel = UILabel(frame: CGRect(x: 20, y: 400, width: 100, height: 40))
        //formLabel.backgroundColor = .systemBlue
        var userField = UITextField(frame: CGRect(x: screenWidth/2-150, y: 100, width: 300, height: 40))
        userField.backgroundColor = .systemBlue
        userField.alpha = 0.5
        userField.returnKeyType = .done
        userField.becomeFirstResponder()
        userField.delegate = self
        userField.autocorrectionType = .no
        //userField.center = self.center
        
        let instructLabel = UILabel(frame: CGRect(x: screenWidth/2-150, y: 50, width: 300, height: 40))
        instructLabel.text = "Please provide an Arabic verb"// + String(globalResults.currWords)
        //var formSubmit = UIButton(frame: CGRect(x: 20, y:160, width: 80, height: 40))
        //formSubmit.setTitle("Deduct!", for: .normal)
        
        view.addSubview(userField)
        view.addSubview(instructLabel)
        

        
    }
    
    @objc func onTap(sender: UIButton) {
        print("tapped")
        let story = UIStoryboard(name: "Main", bundle: nil)
        let controller = story.instantiateViewController(identifier: "SecondController") as! SecondController
       // self.present(controller, animated: true, completion: nil)
        let navigation = UINavigationController(rootViewController: controller)
        self.view.addSubview(navigation.view)
        
        //sc
        self.addChild(navigation)
        let wikiButton = UIButton(frame: CGRect(x: 200, y: 80, width: 200, height: 40))
        wikiButton.setTitle(localResults?.possible_words[sender.tag-1].word, for: .normal)
        wikiButton.titleLabel?.font = UIFont.boldSystemFont(ofSize: 32)
        wikiButton.setTitleColor(.blue, for: .normal)
        wikiButton.addTarget(self, action: #selector(onTapWiki), for: .touchUpInside)
        
        self.view.addSubview(wikiButton)
        let formLabel = UILabel(frame: CGRect(x: 100, y: 150, width: 220, height: 50))
        formLabel.text = localResults?.possible_words[sender.tag-1].form
        self.view.addSubview(formLabel)
        let rootLabel = UILabel(frame: CGRect(x: 250, y: 225, width: 220, height: 50))
        rootLabel.text = localResults?.possible_words[sender.tag-1].root
        self.view.addSubview(rootLabel)
//        let infoLabel = UITextView(frame: CGRect(x: 100, y: 400, width: 300, height: 150))
//        infoLabel.backgroundColor = .systemBlue
//        infoLabel.text = globalResults?.possible_words[sender.tag-1].features
        currentWord = localResults?.possible_words[sender.tag-1]
        //this is going to be a whole chunk of code!! about the stack view let's go
//        var stackView: UIStackView{
//            let stack = UIStackView()
//            stack.axis = .vertical
//            stack.spacing = 20.0
//            stack.alignment = .fill
//            stack.distribution = .fillEqually
//
//            let stackList: Array<UILabel>
            var count = 0
            let featureSet = localResults?.possible_words[sender.tag-1].features
            for feat in featureSet ?? [] {
                count += 1
                let featureLabel = UILabel(frame: CGRect(x: 20, y: 240 + 60 * count, width: Int(self.view.frame.size.width) - 20, height: 80))
                
                let gender = feat.gender
                let mood = feat.mood
                //let person = feat.person
                var plural: String
                var person: String
                let tense = feat.tense
                switch (feat.person) {
                case 1:
                    person = "1st"
                case 2:
                    person = "2nd"
                case 3:
                    person = "3rd"
                default:
                    person = "unknown"
                }
                switch (feat.person) {
                case 1:
                    plural = "singular"
                case 2:
                    plural = "dual"
                case 3:
                    plural = "plural"
                default:
                    plural = "unknown"
                }
                featureLabel.text = String(format: "%@ tense, in %@ person, %@ in gender, %@, and in the %@ mood", tense, person, gender, plural, mood)
                //stackList.append(featureLabel)
                featureLabel.numberOfLines = 3
                self.view.addSubview(featureLabel)
            }
//            stackList.forEach
//
//
//`
//
//        }
        //add the defective flag
        
        if ((localResults?.possible_words[sender.tag-1].weak) != nil){
            if localResults?.possible_words[sender.tag-1].weak == true{
                let weakButton = UIButton(frame: CGRect(x: 120, y: 225, width: 20, height: 20))
                //weakButton.backgroundColor = .systemGray
                weakButton.setImage(UIImage(systemName: "info.circle.fill"), for: .normal)
                weakButton.addTarget(self, action: #selector(onTapWeak), for: .touchUpInside)
                self.view.addSubview(weakButton)
                
                
                //let testlabel = UILabel(frame: CGRect(x: 40, y: 100, width: 20, height: 20))
                
            }
            
        }
                
        //controller.globalResults = globalResults
        // this has to go after adding all the labels
        navigation.didMove(toParent: self)
        
    }

    
    @objc func onTapWiki(sender:UIButton) {
        print("tapped123")
        let verb1: String!
        let verb_encoded: String
        
        let title = sender.titleLabel!
    
        verb1 = String(title.text!)
        //print(verb1)
        
        verb_encoded = verb1.addingPercentEncoding(withAllowedCharacters: CharacterSet.urlQueryAllowed)!
        //print(verb_encoded)
       
        let url_possible = "https://en.wiktionary.org/wiki/" + verb_encoded
        
        if let url = URL(string: url_possible){
            UIApplication.shared.open(url)
        }
       // UIApplication.shared.open(NSURL(string: "http://www.google.com")! as URL)
       
        
    }
    
    @objc func onTapWeak(){
        print("tapped weak")
        var weakType = "weak"
//
        if currentWord != nil{
            
            
            if ((currentWord?.defective) != nil){
                if currentWord?.defective == true{
                weakType = "defective"
                }
            }
            if ((currentWord?.hollow) != nil){
                if currentWord?.hollow == true{
                weakType = "hollow"
                }
            }
            if ((currentWord?.geminated) != nil){
                if currentWord?.geminated == true {
                weakType = "geminated"
                }
            }
        }
        print(weakType)
        let infoString = String(format: "This word may be %@", weakType)
        
        let rectanglePopup = UIView(frame: CGRect(x: 140, y: 245, width: 200, height: 50))
        rectanglePopup.backgroundColor = .systemGray
        let infoLabel = UILabel(frame: CGRect(x: 5, y: 0, width: 200, height: 50))
        infoLabel.text = infoString
        infoLabel.numberOfLines = 2
        rectanglePopup.addSubview(infoLabel)
        self.view.addSubview(rectanglePopup)
        DispatchQueue.main.asyncAfter(deadline: .now() + 2) {
            // your code here delayed by 0.5 seconds
            rectanglePopup.removeFromSuperview()
        }
        
    }

    
    
    func removeAllButtons(){
        for tagNum in [1, 2, 3, 4, 5] {
            if let viewWithTag = self.view.viewWithTag(tagNum) {
                viewWithTag.removeFromSuperview()
            }
        }
        
    }


}

func linkListReturn(str: String) -> Array<String> {
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
struct Affix: Codable{
    let arabic: String
    let meaning: String
}
struct MyResult: Codable{
    let input: String
    let word: String
    let form: String
    let features: Array<Feature>
    let root: String
    let weak: Bool
    let suffixes: Array<Affix>
    let prefixes: Array<Affix>
    let defective: Bool
    let geminated: Bool
    let hollow: Bool
    
    
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
           // formLabel.text = text
            removeAllButtons()
            
            let verb_test: String
            let verb_encoded: String
            verb_test = text
            print(verb_test)
            verb_encoded = verb_test.addingPercentEncoding(withAllowedCharacters: .urlHostAllowed)!
            print(verb_encoded)
            //let url = "http://127.0.0.1:5000/api/verb?id=" + verb_encoded
            let url = "https://qt3-arabic-deduction.herokuapp.com/api/verb?id=" + verb_encoded
            
            
            getData(from: url){ [self] results in
                
                //var test_help: String
                switch results {
                case .failure(let error):
                    print(error.localizedDescription)

                case .success(let response):
                    print (response)
                    var count = 1
                    //self.globalResults.$currWords = "Sup Worlds!"
                    globalResults.currWords += 1
                    localResults = response
                    for item in response.possible_words{
                        let button: UIButton = UIButton()
                        button.setTitle(item.word, for: .normal)
                        button.tag = count
                        button.setTitleColor(.blue, for: .normal)
                        button.frame = CGRect(x: 20, y: 100 + 50 * count, width: 200, height: 20)
                        count += 1
                        button.addTarget(self, action: #selector(onTap(sender:)), for: .touchUpInside)
                        view.addSubview(button)
                        
                    

                      
                    }
                    
       
                }
                
            }
            
            //label.text = help
            
            
            //print("\(text)")
        }
        
        return true
    }
}
//*/
//class CurrentWords: ObservableObject{
//    @Published var result: MyResults
//}
