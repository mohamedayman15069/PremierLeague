import React from "react";
import { Route } from "react-router-dom";

import PlayersList from "./containers/PlayersListView";
import ReviewsList from "./containers/ReviewsListView";
import MatchList from "./containers/MatchListView";
import TeamList from "./containers/TeamsListView";
import LoginForm from "./components/LoginForm";
import LogoutForm from "./components/LogoutForm";
import RegistrationForm from "./components/RegistrationForm";
import ReviewForm from "./components/ReviewsForm";
import playerDetail from "./containers/PlayerDetailView";
import TeamDetail from "./containers/TeamDetailView";
import TopTen from "./containers/TopTenListView";
import UserDetail from "./containers/UserDetailView";
import WinTeam from "./containers/WinTeamView";
import NotFoundPage from "./components/PageNotFound";
import StadiumList from "./containers/StadiumListView";
import StadiumDetail from "./containers/StadiumDetailView";

//This part with Post

import GoogleSearch from "./components/search";

const BaseRouter = () => (
  <div>
    <Route exact path="/login/" component={LoginForm} />
    <Route exact path="/logout/" component={LogoutForm} />
    <Route exact path="/register/" component={RegistrationForm} />
    <Route exact path="/matches" component={MatchList} />
    <Route exact path="/teams/" component={TeamList} />
    <Route exact path="/players/" component={PlayersList} />
    <Route exact path="/players/:playerName/" component={playerDetail} />
    <Route exact path="/teams/:TeamName/" component={TeamDetail} />
    <Route exact path="/" component={TopTen}></Route>

    <Route
      exact
      path="/matches/:season/:homeClubName/:awayClubName/allreview/"
      component={ReviewsList}
    />
    <Route
      exact
      path="/matches/:season/:homeClubName/:awayClubName/"
      component={ReviewForm}
    />

    <Route exact path="/user/:eMail/" component={UserDetail} />

    <Route exact path="/winningteams/" component={WinTeam} />

    <Route exact path="/search/" component={GoogleSearch} />
    <Route exact path="/stadiums/" component={StadiumList} />
    <Route exact path="/stadiums/:StadiumName/" component={StadiumDetail} />
  </div>
);

export default BaseRouter;
