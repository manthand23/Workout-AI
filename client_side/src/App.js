import "./App.css"
import "./index.css"
import Home from "./HomePage.js"
import Analyzer from "./PushUpAnalyzer.js"
import {BrowserRouter as Router, Route, Switch} from "react-router-dom";

function App() {
  return (
    <Router>
      <div className="content">
        <Switch>
          <Route exact path="/">
            <Home />
          </Route>
          <Route path="/push-up-analyzer">
            <Analyzer />
          </Route>
        </Switch>
      </div>
    </Router>
  )
}

export default App;
