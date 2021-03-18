import React, {useEffect, useState} from "react";
import {Button, Container, Form, Navbar} from "react-bootstrap";
import {LinkContainer} from "react-router-bootstrap";
import {Link, Redirect, Route, Switch} from "react-router-dom";

import {logIn, logOut, isLoggedIn} from "./services/AuthService";

import SignUp from "./components/SignUp";
import LogIn from "./components/LogIn";
import Lectures from "./components/Lectures";
import Profile from "./components/Profile";
import LectureDetail from "./components/LectureDetail";
import LessonDetail from "./components/LessonDetail";

import "./App.css";

function App() {
    const [loggedIn, setLoggedIn] = useState(isLoggedIn());

    // useEffect(() => {
    //     setLoggedIn(isLoggedIn());
    // }, []);

    return (
        <>
            <Navbar bg="light" expand="sm" variant="light">
                <LinkContainer to="/">
                    <Navbar.Brand className="logo">
                        Homework Checker
                    </Navbar.Brand>
                </LinkContainer>
                <Navbar.Toggle />
                <Navbar.Collapse>
                    {loggedIn && (
                        <Form inline className="ml-auto">
                            <Link
                                id="lectures"
                                className="btn"
                                to="/lectures/"
                            >
                                Lectures
                            </Link>
                            <Link
                                id="profile"
                                className="btn"
                                to="/profile/"
                            >
                                Profile
                            </Link>
                            <Button type="button" onClick={() => logOut()}>
                                Log out
                            </Button>
                        </Form>
                    )}
                </Navbar.Collapse>
            </Navbar>
            <Container className="pt-3">
                <Switch>
                    <Route
                        exact
                        path="/"
                    >
                        <div className="middle-center">
                            <h1 className="landing logo">
                                Homework Checker
                                </h1>
                            {!loggedIn && (
                                <Link
                                    id="signUp"
                                    className="btn btn-primary mx-2"
                                    to="/signup"
                                >
                                    Sign up
                                </Link>
                            )}
                            {!loggedIn && (
                                <Link
                                    id="logIn"
                                    className="btn btn-primary mx-2"
                                    to="/login"
                                >
                                    Log in
                                </Link>
                            )}
                        </div>
                    </Route>
                    <Route
                        path="/signup"
                    >
                        {loggedIn ? <Redirect to="/" /> : <SignUp />}
                    </Route>
                    <Route
                        path="/login"
                    >
                        {loggedIn ? (
                            <Redirect to="/" />
                        ) : (
                            <LogIn
                                logIn={(email, password) =>
                                    logIn(email, password, setLoggedIn)
                                }
                            />
                        )}
                    </Route>
                    <Route
                        path="/profile/"
                    >
                        {loggedIn ? <Profile /> : <Redirect to="/" />}
                    </Route>
                    <Route
                        path="/lectures/:lecture_slug/:lesson_slug/"
                    >
                        {loggedIn ? <LessonDetail /> : <Redirect to="/" />}
                    </Route>
                    <Route
                        path="/lectures/:lecture_slug/"
                    >
                        {loggedIn ? <LectureDetail /> : <Redirect to="/" />}
                    </Route>
                    <Route
                        path="/lectures/"
                    >
                        {loggedIn ? <Lectures /> : <Redirect to="/" />}
                    </Route>
                </Switch>
            </Container>
        </>
    );
}

export default App;
