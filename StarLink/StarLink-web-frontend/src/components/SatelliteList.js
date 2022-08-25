import React, { Component } from 'react';
import { List, Avatar, Button, Checkbox, Spin } from 'antd';
import satellite from '../assets/images/satellite.svg';

class SatelliteList extends Component {
    constructor() {
        super();
        this.state = {
            selected: [],
            isLoad: false,
        };
    }

    onChange = (e) => {
        console.log('onchange');
        const { dataInfo, checked } = e.target;
        const { selected } = this.state;
        const list = this.addOrRemove(dataInfo, checked, selected);
        this.setState({ selected: list });
    };

    addOrRemove = (item, status, list) => {
        console.log('addOrRemove ->',list);
        const found = list.some((entry) => entry.satid === item.satid);
        if (status && !found) {
            list = [...list, item];
        }

        if (!status && found) {
            list = list.filter((entry) => {
                return entry.satid !== item.satid;
            });
        }
        return list;
    };

    onShowSatMap = () => {
        this.props.onShowMap(this.state.selected);
    };

    render() {
        const satList = this.props.satInfo ? this.props.satInfo.above : [];
        const { isLoad } = this.props;
        const { selected } = this.state;

        return (
            <div className="sat-list-box">
                <Button
                    className="sat-list-btn"
                    size="large"
                    disabled={selected.length === 0}
                    onClick={this.onShowSatMap}
                >
                    Track
                </Button>
                <hr />

                {isLoad ? (
                    <div className="spin-box">
                        <Spin tip="Loading..." size="large" />
                    </div>
                ) : (
                    <List
                        className="sat-list"
                        itemLayout="horizontal"
                        size="small"
                        dataSource={satList}
                        renderItem={(item) => (
                            <List.Item
                                actions={[
                                    <Checkbox dataInfo={item} onChange={this.onChange} />,
                                ]}
                            >
                                <List.Item.Meta
                                    avatar={<Avatar size={50} src={satellite} />}
                                    title={<p>{item.satname}</p>}
                                    description={`Launch Date: ${item.launchDate}`}
                                />
                            </List.Item>
                        )}
                    />
                )}
            </div>
        );
    }
}

export default SatelliteList;
