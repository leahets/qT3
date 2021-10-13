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
        
        let url = "http://api.sunrise-sunset.org/json?date=2020-01-01&lat=-74.0060&lng=40.7128&formatted=0"
        getData(from: url)
    }
    
    @IBAction func buttonTapped(){
        field.resignFirstResponder()
    }

    private func getData(from url: String){
        let task = URLSession.shared.dataTask(with: URL(string: url)!,completionHandler: {data, response, error in
            guard let data = data, error == nil else {
                print("something went wrong")
                return
            }
            //have data
            var result: Response?
            do{
                result = try JSONDecoder().decode(Response.self, from: data)
            }
            catch{
                print("failed to convert \(error.localizedDescription)")
            }
            guard let json = result else {
                return
            }
            print(json.status)
            print(json.results.sunrise)
            print(json.results.sunset)
             
        })
        task.resume()
    }
    struct Response: Codable {
        let results: MyResult
        let status: String
    }
    struct MyResult: Codable{
        let sunrise: String
        let sunset: String
        let solar_noon: String
        let day_length: Int
        let civil_twilight_begin: String
        let civil_twilight_end: String
        let nautical_twilight_begin: String
        let nautical_twilight_end: String
        let astronomical_twilight_begin: String
        let astronomical_twilight_end: String
        
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
