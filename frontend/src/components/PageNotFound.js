import React from 'react';
import { Link } from 'react-router-dom';
class NotFoundPage extends React.Component{
    render(){
        return (
            
            <body>
            
                <div id="notfound">
                    <div class="notfound">
                        <div class="notfound-404">
                            <h1>:(</h1>
                        </div>
                        <h2>404 - Page not found</h2>
                        <p>The page you are looking for might have been removed had its name changed or is temporarily unavailable.</p>
                        <a href="#">home page</a>
                    </div>
                </div>
            
            </body>
            
            



        );
    }
}
export default NotFoundPage;