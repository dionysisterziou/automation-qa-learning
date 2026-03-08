def validate_comment(comment, expected_post_id):

    # shape check
    assert isinstance(comment, dict), f"Expected 'comment' to be dict, got {type(comment)}"
    
    # postId
    assert "postId" in comment, "Missing 'postId'"
    assert isinstance(comment["postId"], int), f"Expected 'postId' to be int, got {type(comment['postId'])}"
    assert comment["postId"] == expected_post_id, f"Expected postId {expected_post_id}, got {comment['postId']}"

    # id
    assert "id" in comment, "Missing 'id'"
    assert isinstance(comment["id"], int), f"Expected 'id' int, got {type(comment['id'])}"
    assert comment["id"], "Empty 'id'"

    # email
    assert "email" in comment, "Missing 'email'"
    assert isinstance(comment["email"], str), f"Expected 'email' to be str, got {type(comment['email'])}"
    assert comment["email"], "Empty 'email'"

    # body
    assert "body" in comment, "Missing 'body'"
    assert isinstance(comment["body"], str), f"Expected 'body' to be str, got {type(comment['body'])}"
    assert comment["body"], "Empty 'body'"

    # name
    assert "name" in comment, "Missing 'name'"
    assert isinstance(comment["name"], str), f"Expected 'name' to be str, got {type(comment['name'])}"
    assert comment["name"], "Empty 'name'"