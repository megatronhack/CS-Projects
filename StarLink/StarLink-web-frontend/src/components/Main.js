import React, { Component } from 'react';
import { Row, Col } from 'antd';
import axios from 'axios';

import SatSetting from './SatSetting';
import SatelliteList from './SatelliteList';
import WorldMap from './WorldMap';
import {
    SAT_API_KEY,
    BASE_URL,
    NEARBY_SATELLITE,
    STARLINK_CATEGORY,
} from '../constants';

class Main extends Component {
    state = {
        setting: {},
        satInfo: {},
        satList: [],
        isLoadingList: false,
    };

    showNearbySatellite = (setting) => {
        console.log('show nearby');
        this.setState({
            setting: setting,
        });
        this.fetchSatellite(setting);
    };

    fetchSatellite = (setting) => {
        console.log('fetching');
        const { latitude, longitude, elevation, altitude } = setting;
        const url = `${BASE_URL}/${NEARBY_SATELLITE}/${latitude}/${longitude}/${elevation}/${altitude}/${STARLINK_CATEGORY}/&apiKey=${SAT_API_KEY}`;

        this.setState({
            isLoadingList: true,
        });

        axios
            .get(url)
            .then((res) => {
                console.log(res.data);
                this.setState({
                    satInfo: res.data,
                    isLoadingList: false,
                });
            })
            .catch((error) => {
                this.setState({
                    isLoadingList: true,
                });
                console.log('err in fetch satellite -> ', error);
            });
    };

    showMap = (selected) => {
        console.log("select array ->", selected)
        this.setState((preState) => ({
            ...preState,
            satList: [...selected],
        }));
    };

    render() {
        const { satInfo, isLoadingList, satList, setting } = this.state;

        return (
            <Row className="main">
                <Col span={8} className="left-side">
                    <SatSetting onShow={this.showNearbySatellite} />
                    <SatelliteList
                        satInfo={satInfo}
                        isLoad={isLoadingList}
                        onShowMap={this.showMap}
                    />
                </Col>
                <Col span={16} className="right-side">
                    <WorldMap satData={satList} observerData={setting} />
                </Col>
            </Row>
        );
    }
}

export default Main;
