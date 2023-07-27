import "./App.css"
import "./index.css"
import React, { useEffect, useState } from "react";
import axios from 'axios';
import Webcam from 'react-webcam';

function PushUpAnalyzer() {

  const [feedback, setFeedback] = useState("");

  const [counter, setCounter] = useState(0);
  const [secondsLeft, setSecondsLeft] = useState(15);
  const [displayMessage, setDisplayMessage] = useState('Start Your Pushups In ');
  const [frameNumber, setFrameNumber] = useState(0);

  const webcamRef = React.useRef(null);
  const videoConstraints = {
    width : 1920,
    height : 1080,
    facingMode: 'user'
  };

  const[name, setName] = useState('')

  const capture = React.useCallback(
  () => {
    const imageSrc = webcamRef.current.getScreenshot();
    //console.log(`imageSrc = ${imageSrc}`)
    axios.post('http://127.0.0.1:5000/api', {data : imageSrc})
    	  .then(res => {
      	  //console.log(`response = ${res.data}`)
      	  setName(res.data)
          //console.log(name)
          if (name === 0) {
            setFeedback("Feedback: You need to straighten your back!")
          } else if (name === 1) {
            setFeedback("Feedback: You're doing great!")
          } else if (name === 2) {
            setFeedback("Analyzing...")
          }
    })
    	  .catch(error => {
      	  console.log(`error = ${error}`)
    })
  }, 
   [webcamRef, name]
  );

  useEffect (() => {
    if (secondsLeft > 0) {
      setTimeout(() => setSecondsLeft(secondsLeft - 1), 1000)
    } else {
      if (counter === 0) {
        setDisplayMessage("Start Doing Pushups Now!")
        setSecondsLeft(30)
        setCounter(1)
      } else {
        setDisplayMessage("Great Job!")
        setSecondsLeft("Complete")
        setFeedback("")
      }
    }
  }, [secondsLeft, counter])

  useEffect (() => {
    if (counter === 1) {
      setTimeout(() => {
        capture()
        setFrameNumber(frameNumber + 1)
      }, 100)
    }
  }, [counter, frameNumber])

  return (
    <div className="App">
      <div className="camera">
        <Webcam
          audio = {false}
          height = {650}
          ref = {webcamRef}
          screenshotFormat = "image/jpeg"
          width = {1300}
          videoConstraints = {videoConstraints}
        />
        <br></br>
        <h1 align="center" style={{color: 'white'}}>
          {displayMessage} [{secondsLeft}]
          <br></br>
          {feedback}
        </h1>
      </div>
    </div>
  )
}

export default PushUpAnalyzer;
