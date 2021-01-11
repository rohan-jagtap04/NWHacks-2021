import React from "react";

function NavBar() {
  return (
    <div>
      <nav class="navbar navbar-expand-md navbar-light fixed-top">
        <a class="navbar-brand nav-link disabled" id="navbar-name">Xalta</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarCollapse">
          <ul class="navbar-nav mr-auto">
            <li class="nav-item"><a class="nav-link" href="#">Home</a></li>
            <li class="nav-item"><a class="nav-link" href="#about">About</a></li>
            <li class="nav-item"><a class="nav-link" href="#webApp">Web App</a></li>
          </ul>
        </div>
      </nav>
    </div>
  );
}

export default NavBar;