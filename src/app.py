from flask import Flask, jsonify, request
from datastructures import FamilyStructure

app = Flask(__name__)
jackson_family = FamilyStructure('Jackson')

@app.route('/members', methods=['GET'])
def get_all_members():
    return jsonify(jackson_family.get_all_members()), 200

@app.route('/member/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = jackson_family.get_member(member_id)
    if member:
        return jsonify(member), 200
    return jsonify({"error": "Member not found"}), 404

@app.route('/member', methods=['POST'])
def add_member():
    new_member = request.json
    if not new_member:
        return jsonify({"error": "Invalid request body"}), 400
    jackson_family.add_member(new_member)
    return jsonify({"message": "Member added successfully"}), 200

@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    member = jackson_family.get_member(member_id)
    if member:
        jackson_family.delete_member(member_id)
        return jsonify({"done": True}), 200
    return jsonify({"error": "Member not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)