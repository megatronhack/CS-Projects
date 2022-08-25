import React, {Component} from 'react';
import {Form, Button, InputNumber} from 'antd';

class SatSetting extends Component {
    showSatellite = values => {
        console.log('Received values of form: ', values);
        this.props.onShow(values);
    }

    render() {
        return (
            <Form
                name="wrap"
                labelCol={{
                    flex: '110px',
                }}
                labelAlign="left"
                labelWrap
                wrapperCol={{
                    flex: 1,
                }}
                colon={false}
                className="sat-setting"
                onFinish={this.showSatellite}
            >

                <Form.Item
                    label="Longitude(degrees)"
                    name="longitude"
                    initialValue = {70}
                    rules={[
                        {
                            required: true,
                            message: "Please input your Longitude",
                        }
                    ]}
                >
                    <InputNumber min={-180} max={180}
                                 style={{width: "100%"}}
                                 placeholder="Please input Longitude"
                    />
                </Form.Item>

                <Form.Item
                    label="Latitude(degrees)"
                    name="latitude"
                    initialValue = {-40}
                    rules={[
                        {
                            required: true,
                            message: "Please input your Latitude",
                        }
                    ]}
                >
                    <InputNumber min={-90} max={90}
                                 style={{width: "100%"}}
                                 placeholder="Please input Longitude"
                    />
                </Form.Item>

                <Form.Item
                    label="Elevation(meters)"
                    name="elevation"
                    initialValue = {100}
                    rules={[
                        {
                            required: true,
                            message: "Please input your Elevation",
                        }
                    ]}
                >
                    <InputNumber min={-413} max={8850}
                                 style={{width: "100%"}}
                                 placeholder="Please input Longitude"
                    />
                </Form.Item>

                <Form.Item
                    label="Altitude(degrees)"
                    name="altitude"
                    initialValue = {90}
                    rules={[
                        {
                            required: true,
                            message: "Please input your Altitude",
                        }
                    ]}
                >
                    <InputNumber min={0} max={90}
                                 style={{width: "100%"}}
                                 placeholder="Please input Longitude"
                    />
                </Form.Item>

                <Form.Item
                    label="Duration(secs)"
                    name="duration"
                    rules={[
                        {
                            required: true,
                            message: "Please input your Duration",
                        }
                    ]}
                >
                    <InputNumber min={0}
                                 max={90}
                                 style={{width: "100%"}}
                                 placeholder="Please input Longitude"
                    />
                </Form.Item>

                <Form.Item className="show-nearby">
                    <Button type="primary"
                            htmlType="submit"
                            style={{textAlign: "center"}}
                    >
                        Find Satellite
                    </Button>
                </Form.Item>

            </Form>
        );
    }
}

export default SatSetting;
