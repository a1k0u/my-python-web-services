questions = [
    "Изобрази удивление и поделись селфи",
    "Сфотографируйтесь с первым попавшимся человеком",
    "Сфотографируй то, что вызывает у тебя улыбку",
    "Отправьте последнее фото из вашей галереи",
    "Поделись улыбкою своей",
]


def __validate_data(task_count: int) -> bool:
    """
    __validate_data
        Task count have to be positive.

    Args:
        task_count (int)

    Returns:
        bool
            False if data is invalid.
            True if it is valid.
    """

    return False if task_count < 0 else True


def get_task(task_count: int) -> tuple[str, bool]:
    """
    get_task
        Returs task from pool.
        If task_count more that questions in the list,
        number will take with mod length if questions.

    Args:
        task_count (int)

    Returns:
        tuple[str, bool]
    """

    if is_valid := __validate_data(task_count):
        return questions[(task_count // 2) % len(questions)], is_valid
    return "Validation error", is_valid
