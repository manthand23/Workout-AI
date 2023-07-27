import "./App.css";
import "./index.css";
import { Link } from "react-router-dom";
import Typical from "react-typical"

function HomePage () {

    return ( 
        <div className="homepage">
            <div className="title">
                <h1>
                    This is{' '}
                    <Typical
                        loop={1}
                        wrapper="b"
                        steps={[
                            "innovation", 1500,
                            "your new trainer", 1500, 
                            "Gymspiration", 1500
                        ]}
                    />.
                </h1>
            </div>
            <br></br>
            <hr size="10" width="85%" color="white"></hr>
            <br></br>
            <Link to="/push-up-analyzer" className="button" data-inline="true">Push Ups</Link>
        </div>
    );
}
 
export default HomePage;