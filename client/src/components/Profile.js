import React, { useEffect, useState } from "react";
import { Card, Col, Row, ListGroup } from "react-bootstrap";
import BreadcrumbWrapper from "./BreadcrumbWrapper";
import { callAPI } from "../services/APIServices";

export default function Profile() {
    const breadcrumbs = [
        { name: "Home", active: false, href: "/" },
        { name: "Profile", active: true }
    ];
    const [data, setData] = useState({
        email: "",
        full_name: "",
        identifier: "",
        enrolled_lectures: []
    });

    useEffect(() => {
        const fetchAccountStatus = async () => {
            const response = await callAPI(`/api/accounts/profile`, "GET");
            if (response) {
                setData({ ...response.data });
            }
        };
        fetchAccountStatus();
    }, []);

    return (
        <Row>
            <Col lg={12}>
                <BreadcrumbWrapper items={breadcrumbs} />
                <h1>Profile</h1>
                Here you find information about your profile.
                <br />
                <br />
                <Card className="mb-3">
                    <Card.Header>Your profile</Card.Header>
                    <Card.Body>
                        <ListGroup variant="flush">
                            <ListGroup.Item>
                                Name: {data.full_name}
                            </ListGroup.Item>
                            <ListGroup.Item>Email: {data.email}</ListGroup.Item>
                            <ListGroup.Item>
                                Student ID:{" "}
                                {data.identifier
                                    ? data.identifier
                                    : "Not specified"}
                            </ListGroup.Item>
                        </ListGroup>
                    </Card.Body>
                </Card>
            </Col>
        </Row>
    );
}

