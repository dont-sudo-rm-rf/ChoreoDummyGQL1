from flask import Flask, jsonify, request
from ariadne import QueryType, make_executable_schema, graphql_sync

type_defs = """
scalar JSON

type Query {
    getClassByNameJSON(name: String!): JSON
}
"""

query = QueryType()

@query.field("getClassByNameJSON")
def resolve_get_class_by_name_json(*_, name):
    if name == "SAR":
        return {
            "name": "SAR",
            "ownedAttribute": [
                {
                    "aggregation": "composite",
                    "association": "_g7h8i9j0k1l2",
                    "name": "alpha",
                    "type": [
                        {
                            "string_type": "_z1y2x3w4v5u6"
                        }
                    ],
                    "visibility": "private",
                    "xmi_id": "_a1b2c3d4e5f6",
                    "xmi_type": "Property"
                },
                {
                    "aggregation": "composite",
                    "association": "_h8i9j0k1l2m3",
                    "name": "beta",
                    "type": [
                        {
                            "string_type": "_y2x3w4v5u6t7"
                        }
                    ],
                    "visibility": "private",
                    "xmi_id": "_b2c3d4e5f6g7",
                    "xmi_type": "Property"
                },
                {
                    "aggregation": "composite",
                    "association": "_i9j0k1l2m3n4",
                    "name": "gamma",
                    "type": [
                        {
                            "string_type": "_x3w4v5u6t7s8"
                        }
                    ],
                    "visibility": "private",
                    "xmi_id": "_c3d4e5f6g7h8",
                    "xmi_type": "Property"
                },
                {
                    "aggregation": "composite",
                    "association": "_j0k1l2m3n4o5",
                    "name": "delta",
                    "type": [
                        {
                            "string_type": "_w4v5u6t7s8r9"
                        }
                    ],
                    "visibility": "private",
                    "xmi_id": "_d4e5f6g7h8i9",
                    "xmi_type": "Property"
                },
                {
                    "aggregation": "composite",
                    "association": "_k1l2m3n4o5p6",
                    "name": "epsilon",
                    "type": [
                        {
                            "string_type": "_v5u6t7s8r9q0"
                        }
                    ],
                    "visibility": "private",
                    "xmi_id": "_e5f6g7h8i9j0",
                    "xmi_type": "Property"
                },
                {
                    "aggregation": "composite",
                    "association": "_l2m3n4o5p6q7",
                    "name": "zeta",
                    "type": [
                        {
                            "string_type": "_u6t7s8r9q0p1"
                        }
                    ],
                    "visibility": "private",
                    "xmi_id": "_f6g7h8i9j0k1",
                    "xmi_type": "Property"
                }
            ],
            "xmi_id": "_19_0beta_8740266_1506431266904_401346_91146",
            "xmi_type": "Class"
        }
    return None

schema = make_executable_schema(type_defs, query)

app = Flask(__name__)

@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=request
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code

if __name__ == "__main__":
    app.run()
